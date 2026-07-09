(function () {
  "use strict";

  var iconsRoot = document.getElementById("desktop-icons");
  var clock = document.getElementById("clock");

  WindowManager.init({
    windowsLayer: document.getElementById("windows"),
    taskbarItems: document.getElementById("taskbar-items")
  });

  RetroFS.load()
    .then(renderDesktop)
    .catch(function (error) {
      openMessageWindow(
        "Startup Error",
        "The desktop data could not be loaded. Serve the site through a static server so data/filesystem.json can be fetched. " + error.message
      );
    });

  updateClock();
  setInterval(updateClock, 30000);

  function renderDesktop() {
    iconsRoot.innerHTML = "";
    RetroFS.getDesktopItems().forEach(function (item, index) {
      iconsRoot.appendChild(createDesktopIcon(item, index));
    });
  }

  function createDesktopIcon(item, index) {
    var button = document.createElement("button");
    var icon = createIconElement(item, "icon-art");
    var label = document.createElement("span");
    var position = getDefaultIconPosition(index);

    button.className = "desktop-icon";
    button.type = "button";
    button.dataset.itemId = item.id || "";
    button.style.left = position.left + "px";
    button.style.top = position.top + "px";

    label.className = "icon-label";
    label.textContent = item.label || "";

    button.append(icon, label);
    button.addEventListener("dblclick", function () {
      openItem(item);
    });
    enableDesktopIconDrag(button);

    return button;
  }

  function openItem(item) {
    if (item.type === "folder") {
      openFolderWindow(item.path, item);
      return;
    }

    if (item.type === "file") {
      TextViewer.open(item);
      return;
    }

    if (item.type === "link" && item.url) {
      window.open(item.url, "_blank", "noopener");
      return;
    }

    if (item.type === "message") {
      openMessageWindow(item.label || "Message", item.body || "");
    }
  }

  function openFolderWindow(path, sourceItem) {
    var folder = RetroFS.getFolder(path);
    var grid = document.createElement("div");

    if (!folder) {
      openMessageWindow("Folder Not Found", "No folder record exists for " + path + ".");
      return;
    }

    grid.className = "folder-grid";
    (folder.items || []).forEach(function (item) {
      grid.appendChild(createFolderItem(item));
    });

    WindowManager.open({
      title: folder.label || "Folder",
      content: grid,
      width: folder.width || "500px",
      height: folder.height || "340px",
      iconPath: sourceItem && sourceItem.iconPath ? sourceItem.iconPath : folder.iconPath || "assets/icons/directory_closed-1.png",
      icon: sourceItem && sourceItem.icon ? sourceItem.icon : folder.icon,
      iconText: sourceItem && sourceItem.iconText ? sourceItem.iconText : folder.iconText
    });
  }

  function createFolderItem(item) {
    var button = document.createElement("button");
    var icon = createIconElement(item, item.type === "file" ? "file-icon" : "icon-art");
    var label = document.createElement("span");

    button.className = "folder-item";
    button.type = "button";

    label.className = "icon-label";
    label.textContent = item.label || "";

    button.append(icon, label);
    button.addEventListener("dblclick", function () {
      openItem(item);
    });

    return button;
  }

  function openMessageWindow(title, message) {
    WindowManager.open({
      title: title,
      content: createMessage(message),
      width: "460px",
      height: "220px",
      iconPath: "assets/icons/msg_information-2.png"
    });
  }

  function createIconElement(item, className) {
    if (item.iconPath) {
      var image = document.createElement("img");
      image.className = className + " image-icon";
      image.src = item.iconPath;
      image.alt = "";
      image.width = 32;
      image.height = 32;
      image.draggable = false;
      image.setAttribute("aria-hidden", "true");
      return image;
    }

    var icon = document.createElement("span");
    icon.className = className + " " + (item.icon || item.type || "");
    icon.textContent = item.iconText || "";
    icon.setAttribute("aria-hidden", "true");
    return icon;
  }

  function getDefaultIconPosition(index) {
    var rowHeight = 76;
    var columnWidth = 86;
    var maxRows = Math.max(1, Math.floor(iconsRoot.clientHeight / rowHeight));
    var row = index % maxRows;
    var column = Math.floor(index / maxRows);

    return {
      left: 10 + column * columnWidth,
      top: 16 + row * rowHeight
    };
  }

  function enableDesktopIconDrag(button) {
    button.addEventListener("mousedown", function (event) {
      if (event.button !== 0) {
        return;
      }

      event.preventDefault();

      var startX = event.clientX;
      var startY = event.clientY;
      var startLeft = button.offsetLeft;
      var startTop = button.offsetTop;

      selectDesktopIcon(button);
      button.classList.add("is-dragging");

      function move(moveEvent) {
        var nextLeft = startLeft + moveEvent.clientX - startX;
        var nextTop = startTop + moveEvent.clientY - startY;
        var maxLeft = iconsRoot.clientWidth - button.offsetWidth;
        var maxTop = iconsRoot.clientHeight - button.offsetHeight;

        button.style.left = Math.max(0, Math.min(nextLeft, maxLeft)) + "px";
        button.style.top = Math.max(0, Math.min(nextTop, maxTop)) + "px";
      }

      function stop() {
        button.classList.remove("is-dragging");
        button.classList.remove("is-selected");
        button.blur();
        document.removeEventListener("mousemove", move);
        document.removeEventListener("mouseup", stop);
      }

      document.addEventListener("mousemove", move);
      document.addEventListener("mouseup", stop);
    });

    button.addEventListener("touchstart", function (event) {
      if (event.touches.length !== 1) {
        return;
      }

      var touch = event.touches[0];
      var startX = touch.clientX;
      var startY = touch.clientY;
      var startLeft = button.offsetLeft;
      var startTop = button.offsetTop;

      selectDesktopIcon(button);
      button.classList.add("is-dragging");

      function move(moveEvent) {
        var nextTouch = moveEvent.touches[0];
        var nextLeft = startLeft + nextTouch.clientX - startX;
        var nextTop = startTop + nextTouch.clientY - startY;
        var maxLeft = iconsRoot.clientWidth - button.offsetWidth;
        var maxTop = iconsRoot.clientHeight - button.offsetHeight;

        moveEvent.preventDefault();

        button.style.left = Math.max(0, Math.min(nextLeft, maxLeft)) + "px";
        button.style.top = Math.max(0, Math.min(nextTop, maxTop)) + "px";
      }

      function stop() {
        button.classList.remove("is-dragging");
        button.classList.remove("is-selected");
        button.blur();
        document.removeEventListener("touchmove", move);
        document.removeEventListener("touchend", stop);
        document.removeEventListener("touchcancel", stop);
      }

      document.addEventListener("touchmove", move, { passive: false });
      document.addEventListener("touchend", stop);
      document.addEventListener("touchcancel", stop);
    });
  }

  function selectDesktopIcon(button) {
    document.querySelectorAll(".desktop-icon").forEach(function (desktopIcon) {
      desktopIcon.classList.remove("is-selected");
    });
    button.classList.add("is-selected");
  }

  function updateClock() {
    clock.textContent = new Date().toLocaleTimeString([], {
      hour: "numeric",
      minute: "2-digit"
    });
  }
})();

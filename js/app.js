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
    RetroFS.getDesktopItems().forEach(function (item) {
      iconsRoot.appendChild(createDesktopIcon(item));
    });
  }

  function createDesktopIcon(item) {
    var button = document.createElement("button");
    var icon = createIconElement(item, "icon-art");
    var label = document.createElement("span");

    button.className = "desktop-icon";
    button.type = "button";
    button.dataset.itemId = item.id || "";

    label.className = "icon-label";
    label.textContent = item.label || "";

    button.append(icon, label);
    button.addEventListener("click", function () {
      document.querySelectorAll(".desktop-icon").forEach(function (desktopIcon) {
        desktopIcon.classList.remove("is-selected");
      });
      button.classList.add("is-selected");
    });
    button.addEventListener("dblclick", function () {
      openItem(item);
    });

    return button;
  }

  function openItem(item) {
    if (item.type === "folder") {
      openFolderWindow(item.path);
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

  function openFolderWindow(path) {
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
      height: folder.height || "340px"
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
      height: "220px"
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
      image.setAttribute("aria-hidden", "true");
      return image;
    }

    var icon = document.createElement("span");
    icon.className = className + " " + (item.icon || item.type || "");
    icon.textContent = item.iconText || "";
    icon.setAttribute("aria-hidden", "true");
    return icon;
  }

  function updateClock() {
    clock.textContent = new Date().toLocaleTimeString([], {
      hour: "numeric",
      minute: "2-digit"
    });
  }
})();

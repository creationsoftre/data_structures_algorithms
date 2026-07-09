(function () {
  "use strict";

  var windowsLayer = null;
  var taskbarItems = null;
  var nextWindowId = 1;
  var topZ = 10;

  window.WindowManager = {
    init: init,
    open: openWindow,
    focus: focusWindow
  };

  function init(options) {
    windowsLayer = options.windowsLayer;
    taskbarItems = options.taskbarItems;
  }

  function openWindow(config) {
    var id = "window-" + nextWindowId++;
    var win = document.createElement("article");
    var titlebar = document.createElement("header");
    var title = document.createElement("div");
    var close = document.createElement("button");
    var body = document.createElement("div");
    var resizeGrip = document.createElement("button");

    win.className = "window" + (config.className ? " " + config.className : "");
    win.id = id;
    win.style.left = (config.left || 132 + nextWindowId * 18) + "px";
    win.style.top = (config.top || 64 + nextWindowId * 16) + "px";
    win.style.width = config.width || "460px";
    win.style.height = config.height || "320px";
    win.setAttribute("role", "dialog");
    win.setAttribute("aria-label", config.title);

    titlebar.className = "titlebar";
    titlebar.addEventListener("pointerdown", startDrag);

    title.className = "titlebar-title";
    title.textContent = config.title;

    close.className = "titlebar-button";
    close.type = "button";
    close.setAttribute("aria-label", "Close " + config.title);
    close.textContent = "x";
    close.addEventListener("click", function () {
      win.remove();
      taskbarButton.remove();
    });

    body.className = "window-body";
    if (typeof config.content === "string") {
      body.innerHTML = config.content;
    } else if (config.content) {
      body.appendChild(config.content);
    }

    resizeGrip.className = "resize-grip";
    resizeGrip.type = "button";
    resizeGrip.setAttribute("aria-label", "Resize " + config.title);
    resizeGrip.addEventListener("pointerdown", startResize);

    titlebar.append(title, close);
    win.append(titlebar, body, resizeGrip);
    windowsLayer.appendChild(win);

    var taskbarButton = document.createElement("button");
    var taskbarLabel = document.createElement("span");
    taskbarButton.className = "taskbar-item";
    taskbarButton.type = "button";
    taskbarLabel.className = "taskbar-label";
    taskbarLabel.textContent = config.title;
    appendTaskbarIcon(taskbarButton, config);
    taskbarButton.appendChild(taskbarLabel);
    taskbarButton.addEventListener("click", function () {
      focusWindow(win);
    });
    taskbarItems.appendChild(taskbarButton);

    win.addEventListener("pointerdown", function () {
      focusWindow(win);
    });

    focusWindow(win);
    return { element: win, body: body };

    function startDrag(event) {
      if (event.target === close) {
        return;
      }

      focusWindow(win);
      titlebar.setPointerCapture(event.pointerId);

      var startX = event.clientX;
      var startY = event.clientY;
      var rect = win.getBoundingClientRect();
      var desktopRect = windowsLayer.getBoundingClientRect();

      function move(moveEvent) {
        var nextLeft = rect.left - desktopRect.left + moveEvent.clientX - startX;
        var nextTop = rect.top - desktopRect.top + moveEvent.clientY - startY;
        var maxLeft = desktopRect.width - 80;
        var maxTop = desktopRect.height - 28;

        win.style.left = Math.max(0, Math.min(nextLeft, maxLeft)) + "px";
        win.style.top = Math.max(0, Math.min(nextTop, maxTop)) + "px";
      }

      function stop() {
        titlebar.removeEventListener("pointermove", move);
        titlebar.removeEventListener("pointerup", stop);
        titlebar.removeEventListener("pointercancel", stop);
      }

      titlebar.addEventListener("pointermove", move);
      titlebar.addEventListener("pointerup", stop);
      titlebar.addEventListener("pointercancel", stop);
    }

    function startResize(event) {
      event.preventDefault();
      event.stopPropagation();
      focusWindow(win);
      resizeGrip.setPointerCapture(event.pointerId);

      var startX = event.clientX;
      var startY = event.clientY;
      var startWidth = win.offsetWidth;
      var startHeight = win.offsetHeight;
      var startLeft = win.offsetLeft;
      var startTop = win.offsetTop;
      var desktopRect = windowsLayer.getBoundingClientRect();
      var minWidth = parsePixelValue(config.minWidth, 280);
      var minHeight = parsePixelValue(config.minHeight, 180);

      function resize(moveEvent) {
        var maxWidth = desktopRect.width - startLeft;
        var maxHeight = desktopRect.height - startTop;
        var nextWidth = startWidth + moveEvent.clientX - startX;
        var nextHeight = startHeight + moveEvent.clientY - startY;

        win.style.width = Math.max(minWidth, Math.min(nextWidth, maxWidth)) + "px";
        win.style.height = Math.max(minHeight, Math.min(nextHeight, maxHeight)) + "px";
      }

      function stopResize() {
        resizeGrip.removeEventListener("pointermove", resize);
        resizeGrip.removeEventListener("pointerup", stopResize);
        resizeGrip.removeEventListener("pointercancel", stopResize);
      }

      resizeGrip.addEventListener("pointermove", resize);
      resizeGrip.addEventListener("pointerup", stopResize);
      resizeGrip.addEventListener("pointercancel", stopResize);
    }
  }

  function parsePixelValue(value, fallback) {
    var parsed = parseInt(value, 10);
    return Number.isFinite(parsed) ? parsed : fallback;
  }

  function appendTaskbarIcon(button, config) {
    var icon = null;

    if (config.iconPath) {
      icon = document.createElement("img");
      icon.src = config.iconPath;
      icon.alt = "";
      icon.draggable = false;
    } else if (config.icon) {
      icon = document.createElement("span");
      icon.className = "taskbar-icon-glyph " + config.icon;
      icon.textContent = config.iconText || "";
    }

    if (!icon) {
      return;
    }

    icon.className = (icon.className ? icon.className + " " : "") + "taskbar-icon";
    icon.setAttribute("aria-hidden", "true");
    button.appendChild(icon);
  }

  function focusWindow(win) {
    var allWindows = windowsLayer.querySelectorAll(".window");
    var allTaskButtons = taskbarItems.querySelectorAll(".taskbar-item");
    var index = Array.prototype.indexOf.call(allWindows, win);

    allWindows.forEach(function (item) {
      item.classList.remove("is-active");
    });
    allTaskButtons.forEach(function (item) {
      item.classList.remove("is-active");
    });

    win.classList.add("is-active");
    win.style.zIndex = String(++topZ);

    if (allTaskButtons[index]) {
      allTaskButtons[index].classList.add("is-active");
    }
  }
})();

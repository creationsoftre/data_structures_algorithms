(function () {
  "use strict";

  var fsData = {
    desktop: [],
    folders: {}
  };

  window.RetroFS = {
    load: function () {
      return fetch("data/filesystem.json")
        .then(function (response) {
          if (!response.ok) {
            throw new Error(response.status + " " + response.statusText);
          }
          return response.json();
        })
        .then(function (data) {
          fsData.desktop = Array.isArray(data.desktop) ? data.desktop : [];
          fsData.folders = data.folders || {};
        });
    },
    getDesktopItems: function () {
      return fsData.desktop;
    },
    getFolder: function (path) {
      return fsData.folders[path];
    }
  };

  window.TextViewer = {
    open: function (item) {
      var pre = document.createElement("pre");
      var title = item.label || item.path || "File";
      var win = WindowManager.open({
        title: title,
        content: pre,
        width: item.width || "720px",
        height: item.height || "480px",
        className: "code-window"
      });

      pre.className = "code-viewer";
      pre.textContent = "Loading " + title + "...";

      fetch(item.path)
        .then(function (response) {
          if (!response.ok) {
            throw new Error(response.status + " " + response.statusText);
          }
          return response.text();
        })
        .then(function (source) {
          pre.textContent = source;
        })
        .catch(function (error) {
          win.body.innerHTML = "";
          win.body.appendChild(createMessage("Could not load " + item.path + ". " + error.message));
        });
    }
  };

  window.createMessage = function (text) {
    var message = document.createElement("p");
    message.className = "message";
    message.textContent = text;
    return message;
  };
})();

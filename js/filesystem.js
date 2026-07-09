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
      var shell = document.createElement("div");
      var toolbar = document.createElement("div");
      var runButton = document.createElement("button");
      var pre = document.createElement("pre");
      var output = document.createElement("pre");
      var title = item.label || item.path || "File";
      var source = "";
      var win = WindowManager.open({
        title: title,
        content: shell,
        width: item.width || "720px",
        height: item.height || "480px",
        className: "code-window"
      });

      shell.className = "code-shell";
      toolbar.className = "code-toolbar";
      runButton.className = "win98-button";
      runButton.type = "button";
      runButton.textContent = "Run";
      runButton.disabled = true;

      pre.className = "code-viewer";
      pre.textContent = "Loading " + title + "...";

      output.className = "python-output";
      output.textContent = "Python output will appear here.";

      toolbar.appendChild(runButton);
      shell.append(toolbar, pre, output);

      runButton.addEventListener("click", function () {
        runButton.disabled = true;
        output.textContent = "Loading Pyodide and running " + title + "...";

        PythonRunner.run(source)
          .then(function (result) {
            output.textContent = result || "Program finished with no output.";
          })
          .catch(function (error) {
            output.textContent = error.message;
          })
          .finally(function () {
            runButton.disabled = false;
          });
      });

      fetch(item.path)
        .then(function (response) {
          if (!response.ok) {
            throw new Error(response.status + " " + response.statusText);
          }
          return response.text();
        })
        .then(function (loadedSource) {
          source = loadedSource;
          pre.textContent = source;
          runButton.disabled = !isPythonFile(item.path);
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

  function isPythonFile(path) {
    return /\.py$/i.test(path || "");
  }
})();

(function () {
  "use strict";

  var pyodidePromise = null;

  window.PythonRunner = {
    run: runPython
  };

  function loadRuntime() {
    if (pyodidePromise) {
      return pyodidePromise;
    }

    if (typeof loadPyodide !== "function") {
      return Promise.reject(new Error("Pyodide failed to load. Check your network connection."));
    }

    pyodidePromise = loadPyodide();
    return pyodidePromise;
  }

  function runPython(source) {
    return loadRuntime().then(function (pyodide) {
      pyodide.globals.set("__code_desk_source__", source);

      return pyodide.runPythonAsync([
        "import contextlib",
        "import io",
        "import traceback",
        "",
        "__code_desk_stdout__ = io.StringIO()",
        "__code_desk_stderr__ = io.StringIO()",
        "",
        "try:",
        "    with contextlib.redirect_stdout(__code_desk_stdout__), contextlib.redirect_stderr(__code_desk_stderr__):",
        "        exec(__code_desk_source__, globals())",
        "except BaseException:",
        "    traceback.print_exc(file=__code_desk_stderr__)",
        "",
        "__code_desk_stdout__.getvalue() + __code_desk_stderr__.getvalue()"
      ].join("\n"));
    });
  }
})();

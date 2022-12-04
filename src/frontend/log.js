let logn;

let login = button => {
    logn = document.getElementById("loginName").value;

    function log() {
        var requestOptions = {
            method: 'POST',
            redirect: 'follow'
          };

          fetch("http://127.0.0.1:5000/loginUser?userName="+logn+"", requestOptions)
            .then(response => response.text())
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
      };

    log();
    open('index.html');
  };
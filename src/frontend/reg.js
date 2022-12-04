let register = button => {
    let regn = document.getElementById("regname").value;

    function reg() {
        var requestOptions = {
            method: 'POST',
            redirect: 'follow'
          };

          fetch("http://127.0.0.1:5000/registerUser?userName="+regn+"", requestOptions)
            .then(response => response.text())
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
      };

    reg();
  };
const loginFormDiv = document.querySelector('.login-form');
const signupFormDiv = document.querySelector('.signup-form');
const onboardingFormDiv = document.querySelector('.onboarding-form');
const signupLink = document.querySelector('.signup-link');
const loginLink = document.querySelector('.login-link');
const loginForm = document.querySelector('#login-form');
const loginUsername = document.querySelector('#login-name');
const loginPassword = document.querySelector('#login-password');
const signupForm = document.querySelector('#signup-form');
const signupUsername = document.querySelector('#signup-username');
const signupPassword = document.querySelector('#signup-password');
const signupConfirmPassword = document.querySelector('#signup-confirm-password');
const onboardingForm = document.querySelector('#onboarding-form');
const loginButton = document.querySelector('#login-button');
const signupButton = document.querySelector('#signup-button');
const onboardingButton = document.querySelector('#onboarding-button');
const loginSpinner = document.querySelector('#login-spinner');
const signupSpinner = document.querySelector('#signup-spinner');

loginFormDiv.style.display = 'none';
signupFormDiv.style.display = 'block'; // hide the sign-up form initially
onboardingFormDiv.style.display = 'none'; // hide the onboarding form initially

document.querySelector('.javascript-warning').style.display = 'none'; // hide the javascript warning


signupLink.addEventListener('click', handleSignupClick);
loginLink.addEventListener('click', handleLoginClick);

function handleSignupClick(event) {
    event.preventDefault();
    loginFormDiv.style.display = 'none';
    signupFormDiv.style.display = 'block';
}

function handleLoginClick(event) {
    event.preventDefault();
    signupFormDiv.style.display = 'none';
    loginFormDiv.style.display = 'block';
}

function removeListeners() {
    signupLink.removeEventListener('click', handleSignupClick);
    loginLink.removeEventListener('click', handleLoginClick);
}

function addListeners() {
    signupLink.addEventListener('click', handleSignupClick);
    loginLink.addEventListener('click', handleLoginClick);
}

String.prototype.hashCode = function() {
    // This is purely a simple hashing function to prevent the password from being sent in plain text to the server over HTTP
    // This hash is insecure and passwords are not stored in this format on the server
    var hash = 0,
        i, chr;
    if (this.length === 0) return hash;
    for (i = 0; i < this.length; i++) {
        chr = this.charCodeAt(i);
        hash = ((hash << 5) - hash) + chr;
        hash |= 0; // Convert to 32bit integer
    }
    return hash;
};

showOnboarding = (username, code, id, heading) => {
    signupFormDiv.style.display = 'none';
    loginFormDiv.style.display = 'none';
    onboardingFormDiv.style.display = 'block';
    document.querySelector('#welcome').innerText = 'Welcome, ' + username;
    document.querySelector('#id').innerText = id;
    document.querySelector('#onboarding-heading').innerText = heading;
    onboardingButton.addEventListener('click', () => {
        event.preventDefault(); // Prevent the form from submitting
        window.location.href = 'com.epicgames.wex://authorize/?code=' + code;
    });
    return true;
};

signupForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the form from submitting
    let timeoutId;
    signupSpinner.classList.add('show');
    signupButton.disabled = true;
    signupUsername.disabled = true;
    signupPassword.disabled = true;
    signupConfirmPassword.disabled = true;
    removeListeners();
    setTimeout(() => {
        if (signupPassword.value !== signupConfirmPassword.value) {
            alert('Passwords do not match!');
            signupSpinner.classList.remove('show');
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupPassword.value.length < 4) {
            alert('Password must be at least 4 characters long!');
            signupSpinner.classList.remove('show');
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupPassword.value.length > 32) {
            alert('Password must be less than 32 characters long!');
            signupSpinner.classList.remove('show');
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupUsername.value.length < 3) {
            alert('Username must be at least 3 characters long!');
            signupSpinner.classList.remove('show');
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupUsername.value.length > 24) {
            alert('Username must be less than 24 characters long!');
            signupSpinner.classList.remove('show');
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupPassword.value === signupUsername.value) {
            alert('Password cannot be the same as your username!');
            signupSpinner.classList.remove('show');
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else {
            // post to the server
            const signupData = {
                username: document.querySelector('#signup-username').value,
                password: document.querySelector('#signup-password').value.hashCode()
            };
            const controller = new AbortController();
            const signal = controller.signal;

            // set a 10 second timeout
            timeoutId = setTimeout(() => {
                // clear the timeout and show an error message
                clearTimeout(timeoutId);
                alert('Request timed out. Please try again later.');
                signupSpinner.classList.remove('show');
                signupButton.disabled = false;
                signupUsername.disabled = false;
                signupPassword.disabled = false;
                signupConfirmPassword.disabled = false;
                addListeners();
            }, 10000);

            fetch('/id/login/token', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'basic ZWMwZWJiN2U1NmY2NDU0ZTg2YzYyMjk5YTdiMzJlMjE6YmJwcml2YXRlc2VydmVyaW5tZW1vcnlvZmRpcHB5PDM=',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-Request-Source': 'login-script.js',
                    'X-Request-Source-Url': window.location.href,
                    'X-Request-Source-Form': 'signup-form'
                },
                body: JSON.stringify(signupData),
                signal // pass the signal to the fetch request to be able to abort it
            }).then(response => {
                if (response.status === 200) {
                    response.json().then(data => {
                        // window.location.href = '/id/login/onboarding?username=' + signupData.username + '&code=' + data.authorisationCode;
                        showOnboarding(signupData.username, data.authorisationCode, data.id, data.heading);
                        signupSpinner.classList.remove('show');
                    }).catch(() => {
                        alert('An error occurred when trying to log in!\n\nSomething went wrong when redirecting... Please try again later.');
                        signupSpinner.classList.remove('show');
                        signupButton.disabled = false;
                        signupUsername.disabled = false;
                        signupPassword.disabled = false;
                        signupConfirmPassword.disabled = false;
                        addListeners();
                    });
                } else {
                    response.json().then(data => {
                        alert('An error occurred when logging in!\n\nError Info:\n' + data.errorCode + '\n' + data.errorMessage);
                        signupSpinner.classList.remove('show');
                        signupButton.disabled = false;
                        signupUsername.disabled = false;
                        signupPassword.disabled = false;
                        signupConfirmPassword.disabled = false;
                        addListeners();
                    }).catch(() => {
                        alert('An error occurred when trying to login!\n\nError Info:\n' + response.status + ' ' + response.statusText + '\n' + response.body.toString());
                        signupSpinner.classList.remove('show');
                        signupButton.disabled = false;
                        signupUsername.disabled = false;
                        signupPassword.disabled = false;
                        signupConfirmPassword.disabled = false;
                        addListeners();
                    });
                }
            }).catch(error => {
                alert('An error occurred when logging in!\n\nThe request timed out...\n\n' + error);
                signupSpinner.classList.remove('show');
                signupButton.disabled = false;
                signupUsername.disabled = false;
                signupPassword.disabled = false;
                signupConfirmPassword.disabled = false;
                addListeners();
            }).finally(() => {
                clearTimeout(timeoutId); // clear the timeout if the request is completed
                signupSpinner.classList.remove('show');
                signupButton.disabled = false;
                signupUsername.disabled = false;
                signupPassword.disabled = false;
                signupConfirmPassword.disabled = false;
            });
        }
    }, 1000);
});


loginForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the form from submitting
    let timeoutId;
    loginSpinner.classList.add('show');
    loginButton.disabled = true;
    loginUsername.disabled = true;
    loginPassword.disabled = true;
    removeListeners();
    setTimeout(() => {
        if (loginPassword.value.length < 4) {
            alert('Password must be at least 4 characters long!');
            loginSpinner.classList.remove('show');
            loginButton.disabled = false;
            loginUsername.disabled = false;
            loginPassword.disabled = false;
            addListeners();
        } else if (loginPassword.value.length > 32) {
            alert('Password must be less than 32 characters long!');
            loginSpinner.classList.remove('show');
            loginButton.disabled = false;
            loginUsername.disabled = false;
            loginPassword.disabled = false;
            addListeners();
        } else if (loginUsername.value.length < 3) {
            alert('Username must be at least 3 characters long!');
            loginSpinner.classList.remove('show');
            loginButton.disabled = false;
            loginUsername.disabled = false;
            loginPassword.disabled = false;
            addListeners();
            // } else if (loginUsername.value.length > 24) {
            //     // if not trying to enter an account id
            //     if (!loginUsername.value.match(/^[0-9a-fA-F]{32}$/)) {
            //         event.preventDefault(); // Prevent the form from submitting
            //         alert('This account ID is not valid!');
            //     }
        } else if (loginPassword.value === loginUsername.value) {
            alert('Password cannot be the same as your username!');
            loginSpinner.classList.remove('show');
            loginButton.disabled = false;
            loginUsername.disabled = false;
            loginPassword.disabled = false;
            addListeners();
        } else {
            // post to the server
            const loginData = {
                username: document.querySelector('#login-name').value,
                password: document.querySelector('#login-password').value.hashCode()
            };
            const controller = new AbortController();
            const signal = controller.signal;

            // set a 10 second timeout
            timeoutId = setTimeout(() => {
                // clear the timeout and show an error message
                clearTimeout(timeoutId);
                alert('Request timed out. Please try again later.');
                loginSpinner.classList.remove('show');
                loginButton.disabled = false;
                loginUsername.disabled = false;
                loginPassword.disabled = false;
                addListeners();
            }, 10000);

            fetch('/id/login/token', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'basic ZWMwZWJiN2U1NmY2NDU0ZTg2YzYyMjk5YTdiMzJlMjE6YmJwcml2YXRlc2VydmVyaW5tZW1vcnlvZmRpcHB5PDM=',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-Request-Source': 'login-script.js',
                    'X-Request-Source-Url': window.location.href,
                    'X-Request-Source-Form': 'login-form'
                },
                body: JSON.stringify(loginData),
                signal // pass the signal to the fetch request to be able to abort it
            }).then(response => {
                if (response.status === 200) {
                    response.json().then(data => {
                        // console.log('Login successful! Redirecting to /id/login/complete?username=' + data.username + '&code=' + data.authorisationCode);
                        // window.location.href = '/id/login/complete?username=' + data.username + '&code=' + data.authorisationCode;
                        showOnboarding(data.username, data.authorisationCode, data.id, data.heading);
                        loginSpinner.classList.remove('show');
                    }).catch(() => {
                        alert('An error occurred when trying to log in!\n\nSomething went wrong when redirecting... Please try again later.');
                        loginSpinner.classList.remove('show');
                        loginButton.disabled = false;
                        loginUsername.disabled = false;
                        loginPassword.disabled = false;
                        addListeners();
                    });
                } else {
                    response.json().then(data => {
                        alert('An error occurred when logging in!\n\nError Info:\n' + data.errorCode + '\n' + data.errorMessage);
                        loginSpinner.classList.remove('show');
                        loginButton.disabled = false;
                        loginUsername.disabled = false;
                        loginPassword.disabled = false;
                        addListeners();
                    }).catch(() => {
                        alert('An error occurred when trying to login!\n\nError Info:\n' + response.status + ' ' + response.statusText + '\n' + response.body.toString());
                        loginSpinner.classList.remove('show');
                        loginButton.disabled = false;
                        loginUsername.disabled = false;
                        loginPassword.disabled = false;
                        addListeners();
                    });
                }
            }).catch(error => {
                alert('An error occurred when logging in!\n\nThe request timed out...\n\n' + error);
                loginSpinner.classList.remove('show');
                loginButton.disabled = false;
                loginUsername.disabled = false;
                loginPassword.disabled = false;
                addListeners();
            }).finally(() => {
                clearTimeout(timeoutId); // clear the timeout if the request is completed
                loginSpinner.classList.remove('show');
                loginButton.disabled = false;
                loginUsername.disabled = false;
                loginPassword.disabled = false;
            });
        }
    }, 1000);
});

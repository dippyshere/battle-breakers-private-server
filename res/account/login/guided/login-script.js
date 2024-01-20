// var onboardingForm = document.querySelector('#onboarding-form');
var loginFormDiv = document.querySelector(".login-form"),
    signupFormDiv = document.querySelector(".signup-form"),
    onboardingFormDiv = document.querySelector(".onboarding-form"),
    signupLink = document.querySelector(".signup-link"),
    loginLink = document.querySelector(".login-link"),
    loginForm = document.querySelector("#login-form"),
    loginUsername = document.querySelector("#login-name"),
    loginPassword = document.querySelector("#login-password"),
    signupForm = document.querySelector("#signup-form"),
    signupUsername = document.querySelector("#signup-username"),
    signupPassword = document.querySelector("#signup-password"),
    signupConfirmPassword = document.querySelector("#signup-confirm-password"),
    loginButton = document.querySelector("#login-button"),
    signupButton = document.querySelector("#signup-button"),
    onboardingButton = document.querySelector("#onboarding-button"),
    loginSpinner = document.querySelector("#login-spinner"),
    signupSpinner = document.querySelector("#signup-spinner");
loginFormDiv.style.display = "block";
signupFormDiv.style.display = "none"; // hide the sign-up form initially
onboardingFormDiv.style.display = "none"; // hide the onboarding form initially

document.querySelector(".javascript-warning").style.display = "none"; // hide the javascript warning

signupLink.addEventListener("click", handleSignupClick);
loginLink.addEventListener("click", handleLoginClick);

function handleSignupClick(event) {
    "use strict";

    event.preventDefault();
    loginFormDiv.style.display = "none";
    signupFormDiv.style.display = "block";
}

function handleLoginClick(event) {
    "use strict";

    event.preventDefault();
    signupFormDiv.style.display = "none";
    loginFormDiv.style.display = "block";
}

function removeListeners() {
    "use strict";

    signupLink.removeEventListener("click", handleSignupClick);
    loginLink.removeEventListener("click", handleLoginClick);
}

function addListeners() {
    "use strict";

    signupLink.addEventListener("click", handleSignupClick);
    loginLink.addEventListener("click", handleLoginClick);
}

var showOnboarding = function showOnboarding(username, code, id, heading) {
    "use strict";

    signupFormDiv.style.display = "none";
    loginFormDiv.style.display = "none";
    onboardingFormDiv.style.display = "block";
    document.querySelector("#welcome").innerText = "Welcome, " + username;
    document.querySelector("#id").innerText = id;
    document.querySelector("#onboarding-heading").innerText = heading;
    onboardingButton.addEventListener("click", function () {
        event.preventDefault(); // Prevent the form from submitting
        window.location.href = "com.epicgames.wex://authorize/?code=" + code;
    });
    return true;
};
signupForm.addEventListener("submit", function (event) {
    "use strict";

    event.preventDefault(); // Prevent the form from submitting
    var timeoutId;
    signupSpinner.classList.add("show");
    signupButton.disabled = true;
    signupUsername.disabled = true;
    signupPassword.disabled = true;
    signupConfirmPassword.disabled = true;
    removeListeners();
    setTimeout(function () {
        if (signupPassword.value !== signupConfirmPassword.value) {
            signupSpinner.classList.remove("show");
            window.alert("Passwords do not match!");
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupPassword.value.length < 4) {
            signupSpinner.classList.remove("show");
            window.alert("Password must be at least 4 characters long!");
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupPassword.value.length > 64) {
            signupSpinner.classList.remove("show");
            window.alert("Password must be less than 64 characters long!");
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupUsername.value.length < 3) {
            signupSpinner.classList.remove("show");
            window.alert("Username must be at least 3 characters long!");
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupUsername.value.length > 24) {
            signupSpinner.classList.remove("show");
            window.alert("Username must be less than 24 characters long!");
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else if (signupPassword.value === signupUsername.value) {
            signupSpinner.classList.remove("show");
            window.alert("Password cannot be the same as your username!");
            signupButton.disabled = false;
            signupUsername.disabled = false;
            signupPassword.disabled = false;
            signupConfirmPassword.disabled = false;
            addListeners();
        } else {
            // post to the server
            var signupData = {
                username: document.querySelector("#signup-username").value,
                password: document.querySelector("#signup-password").value
            };
            var controller = new window.AbortController();
            var signal = controller.signal;

            // set a 10 second timeout
            timeoutId = setTimeout(function () {
                // clear the timeout and show an error message
                clearTimeout(timeoutId);
                controller.abort();
                signupSpinner.classList.remove("show");
                setTimeout(function () {
                    window.alert("Request timed out. Please try again later.");
                }, 1);
                signupButton.disabled = false;
                signupUsername.disabled = false;
                signupPassword.disabled = false;
                signupConfirmPassword.disabled = false;
                addListeners();
            }, 10000);
            fetch("/id/login/token", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                    Authorization:
                        "basic ZWMwZWJiN2U1NmY2NDU0ZTg2YzYyMjk5YTdiMzJlMjE6YmJwcml2YXRlc2VydmVyaW5tZW1vcnlvZmRpcHB5PDM=",
                    "X-Requested-With": "XMLHttpRequest",
                    "X-Request-Source": "login-script.js",
                    "X-Request-Source-Url": window.location.href,
                    "X-Request-Source-Form": "signup-form"
                },
                body: JSON.stringify(signupData),
                signal: signal // pass the signal to the fetch request to be able to abort it
            })
                .then(function (response) {
                    if (response.status === 200) {
                        response
                            .json()
                            .then(function (data) {
                                // window.location.href = '/id/login/onboarding?username=' + signupData.username + '&code=' + data.authorisationCode;
                                signupSpinner.classList.remove("show");
                                showOnboarding(
                                    signupData.username,
                                    data.authorisationCode,
                                    data.id,
                                    data.heading
                                );
                            })
                            ["catch"](function () {
                            signupSpinner.classList.remove("show");
                            window.alert(
                                "An error occurred when trying to log in!\n\nSomething went wrong when redirecting... Please try again later."
                            );
                            signupButton.disabled = false;
                            signupUsername.disabled = false;
                            signupPassword.disabled = false;
                            signupConfirmPassword.disabled = false;
                            addListeners();
                        });
                    } else {
                        response
                            .json()
                            .then(function (data) {
                                signupSpinner.classList.remove("show");
                                window.alert(
                                    "An error occurred when logging in!\n\n" + data.errorMessage
                                );
                                signupButton.disabled = false;
                                signupUsername.disabled = false;
                                signupPassword.disabled = false;
                                signupConfirmPassword.disabled = false;
                                addListeners();
                            })
                            ["catch"](function () {
                            signupSpinner.classList.remove("show");
                            window.alert(
                                "An error occurred when trying to login!\n\nError Info:\n" +
                                response.status +
                                " " +
                                response.statusText +
                                "\n" +
                                response.body.toString()
                            );
                            signupButton.disabled = false;
                            signupUsername.disabled = false;
                            signupPassword.disabled = false;
                            signupConfirmPassword.disabled = false;
                            addListeners();
                        });
                    }
                })
                ["catch"](function (error) {
                if (error.name === "AbortError") {
                    return;
                }
                signupSpinner.classList.remove("show");
                window.alert("An error occurred when logging in!\n\n" + error);
                signupButton.disabled = false;
                signupUsername.disabled = false;
                signupPassword.disabled = false;
                signupConfirmPassword.disabled = false;
                addListeners();
            })
                ["finally"](function () {
                clearTimeout(timeoutId); // clear the timeout if the request is completed
                signupSpinner.classList.remove("show");
                signupButton.disabled = false;
                signupUsername.disabled = false;
                signupPassword.disabled = false;
                signupConfirmPassword.disabled = false;
            });
        }
    }, 1000);
});
loginForm.addEventListener("submit", function (event) {
    "use strict";

    event.preventDefault(); // Prevent the form from submitting
    var timeoutId;
    loginSpinner.classList.add("show");
    loginButton.disabled = true;
    loginUsername.disabled = true;
    loginPassword.disabled = true;
    removeListeners();
    setTimeout(function () {
        if (loginPassword.value.length < 4) {
            loginSpinner.classList.remove("show");
            window.alert("Password must be at least 4 characters long!");
            loginButton.disabled = false;
            loginUsername.disabled = false;
            loginPassword.disabled = false;
            addListeners();
        } else if (loginPassword.value.length > 64) {
            loginSpinner.classList.remove("show");
            window.alert("Password must be less than 64 characters long!");
            loginButton.disabled = false;
            loginUsername.disabled = false;
            loginPassword.disabled = false;
            addListeners();
        } else if (loginUsername.value.length < 3) {
            loginSpinner.classList.remove("show");
            window.alert("Username must be at least 3 characters long!");
            loginButton.disabled = false;
            loginUsername.disabled = false;
            loginPassword.disabled = false;
            addListeners();
            // } else if (loginUsername.value.length > 24) {
            //     // if not trying to enter an account id
            //     if (!loginUsername.value.match(/^[0-9a-fA-F]{32}$/)) {
            //         event.preventDefault(); // Prevent the form from submitting
            //         window.alert('This account ID is not valid!');
            //     }
        } else if (loginPassword.value === loginUsername.value) {
            loginSpinner.classList.remove("show");
            window.alert("Password cannot be the same as your username!");
            loginButton.disabled = false;
            loginUsername.disabled = false;
            loginPassword.disabled = false;
            addListeners();
        } else {
            // post to the server
            var loginData = {
                username: document.querySelector("#login-name").value,
                password: document.querySelector("#login-password").value
            };
            var controller = new window.AbortController();
            var signal = controller.signal;

            // set a 10 second timeout
            timeoutId = setTimeout(function () {
                // clear the timeout and show an error message
                clearTimeout(timeoutId);
                controller.abort();
                loginSpinner.classList.remove("show");
                setTimeout(function () {
                    window.alert("Request timed out. Please try again later.");
                }, 1);
                loginButton.disabled = false;
                loginUsername.disabled = false;
                loginPassword.disabled = false;
                addListeners();
            }, 10000);
            fetch("/id/login/token", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                    Authorization:
                        "basic ZWMwZWJiN2U1NmY2NDU0ZTg2YzYyMjk5YTdiMzJlMjE6YmJwcml2YXRlc2VydmVyaW5tZW1vcnlvZmRpcHB5PDM=",
                    "X-Requested-With": "XMLHttpRequest",
                    "X-Request-Source": "login-script.js",
                    "X-Request-Source-Url": window.location.href,
                    "X-Request-Source-Form": "login-form"
                },
                body: JSON.stringify(loginData),
                signal: signal // pass the signal to the fetch request to be able to abort it
            })
                .then(function (response) {
                    if (response.status === 200) {
                        response
                            .json()
                            .then(function (data) {
                                // console.log('Login successful! Redirecting to /id/login/complete?username=' + data.username + '&code=' + data.authorisationCode);
                                // window.location.href = '/id/login/complete?username=' + data.username + '&code=' + data.authorisationCode;
                                showOnboarding(
                                    data.username,
                                    data.authorisationCode,
                                    data.id,
                                    data.heading
                                );
                                loginSpinner.classList.remove("show");
                            })
                            ["catch"](function () {
                            loginSpinner.classList.remove("show");
                            window.alert(
                                "An error occurred when trying to log in!\n\nSomething went wrong when redirecting... Please try again later."
                            );
                            loginButton.disabled = false;
                            loginUsername.disabled = false;
                            loginPassword.disabled = false;
                            addListeners();
                        });
                    } else {
                        response
                            .json()
                            .then(function (data) {
                                loginSpinner.classList.remove("show");
                                window.alert(
                                    "An error occurred when logging in!\n\n" + data.errorMessage
                                );
                                loginButton.disabled = false;
                                loginUsername.disabled = false;
                                loginPassword.disabled = false;
                                addListeners();
                            })
                            ["catch"](function () {
                            loginSpinner.classList.remove("show");
                            window.alert(
                                "An error occurred when trying to login!\n\nError Info:\n" +
                                response.status +
                                " " +
                                response.statusText +
                                "\n" +
                                response.body.toString()
                            );
                            loginButton.disabled = false;
                            loginUsername.disabled = false;
                            loginPassword.disabled = false;
                            addListeners();
                        });
                    }
                })
                ["catch"](function (error) {
                if (error.name === "AbortError") {
                    return;
                }
                loginSpinner.classList.remove("show");
                window.alert("An error occurred when logging in!\n\n" + error);
                loginButton.disabled = false;
                loginUsername.disabled = false;
                loginPassword.disabled = false;
                addListeners();
            })
                ["finally"](function () {
                clearTimeout(timeoutId); // clear the timeout if the request is completed
                loginSpinner.classList.remove("show");
                loginButton.disabled = false;
                loginUsername.disabled = false;
                loginPassword.disabled = false;
            });
        }
    }, 1000);
});

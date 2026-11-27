"use strict";

// VERIXA EXCHANGE - Interface principale

document.addEventListener("DOMContentLoaded", () => {
    const menuButton = document.getElementById("menuButton");
    const sidebar = document.getElementById("sidebar");
    const navigationLinks = document.querySelectorAll(".nav-link");

    // Menu mobile
    if (menuButton && sidebar) {
        menuButton.addEventListener("click", () => {
            sidebar.classList.toggle("open");

            menuButton.textContent =
                sidebar.classList.contains("open") ? "✕" : "☰";
        });
    }

    // Navigation entre les sections
    navigationLinks.forEach((link) => {
        link.addEventListener("click", () => {
            navigationLinks.forEach((item) => {
                item.classList.remove("active");
            });

            link.classList.add("active");

            if (sidebar) {
                sidebar.classList.remove("open");
            }

            if (menuButton) {
                menuButton.textContent = "☰";
            }
        });
    });

    // Vérification de la configuration
    console.log("================================");
    console.log("VERIXA EXCHANGE");
    console.log("A New Digital Market.");
    console.log("Interface initialisée.");
    console.log("Mode : SIMULATION");
    console.log("================================");

    // État de démonstration
    const platformState = {
        name: "VERIXA EXCHANGE",
        symbol: "VRX",
        mode: "simulation",
        currencies: ["USD", "XOF", "EUR", "GBP"],
        markets: [
            "COMPUTE",
            "STORAGE",
            "NETWORK",
            "DATA"
        ]
    };

    window.VERIXA = Object.freeze(platformState);
});

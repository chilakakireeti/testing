# Reverse a string

import os
import json
import time

PROJECT_NAME = "express-health-api"

folders = [
    "controllers",
    "routes",
    "models",
    "middleware"
]





files = {

    "package.json": {
        "name": PROJECT_NAME,
        "version": "1.0.0",
        "main": "server.js",
        "scripts": {
            "start": "node server.js",
            "dev": "nodemon server.js"



        },
        "dependencies": {
            "cors": "^2.8.5",
            "dotenv": "^16.4.5",
            "express": "^4.19.2"
        },
        "devDependencies": {
            "nodemon": "^3.1.0"
        }
    },


    ".env": """
PORT=5000
""",


    "server.js": """
const express = require("express");
const cors = require("cors");
require("dotenv").config();

const healthRoutes = require("./routes/healthRoutes");

const app = express();


// Middleware
app.use(cors());
app.use(express.json());


// Routes
app.use("/", healthRoutes);


// Server Port
const PORT = process.env.PORT || 5000;


app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
""",


    "controllers/healthController.js": """
exports.healthCheck = (req, res) => {

    res.status(200).json({
        status: "OK",
        message: "Server is healthy"
    });

};
""",


    "routes/healthRoutes.js": """
const express = require("express");

const router = express.Router();

const {
    healthCheck
} = require("../controllers/healthController");


// GET /health
router.get("/health", healthCheck);


module.exports = router;
""",


    "models/index.js": """
// Database models will be added here
""",


    "middleware/index.js": """
// Custom middleware will be added here and used
"""
}



def project_creation():

    os.makedirs(PROJECT_NAME, exist_ok=True)

    for folder in folders:
        os.makedirs(
            os.path.join(PROJECT_NAME, folder),
            exist_ok=True
        )


    for filename, content in files.items():

        filepath = os.path.join(
            PROJECT_NAME,
            filename
        )


        with open(filepath, "w") as f:

            if isinstance(content, dict):
                json.dump(
                    content,
                    f,
                    indent=4
                )
            else:
                f.write(content.strip())


    print("Project created successfully!")
    print(f"Location: {PROJECT_NAME}/")
    print("\nNext steps:")
    print(f"cd {PROJECT_NAME}")
    print("npm install")
    print("npm start")

def add(a,b):
    return a+b

print(add(5,3))

project_creation()

#data for testing
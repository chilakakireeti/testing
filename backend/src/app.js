const express = require("express");

const dotenv = require("dotenv");

const requestLogger =
    require("./middleware/requestLogger");

const notFound =
    require("./middleware/notFound");

const errorHandler =
    require("./middleware/errorHandler");


const routes =
    require("./routes/testRoutes");



dotenv.config();



const app = express();



/*
 Body parser
*/

app.use(
    express.json()
);



/*
 Request logging
*/

app.use(
    requestLogger
);



/*
 Routes
*/

app.use(
    "/api",
    routes
);




/*
 Unknown route handler
*/

app.use(
    notFound
);



/*
 Global error middleware
 MUST be last
*/

app.use(
    errorHandler
);



module.exports = app;
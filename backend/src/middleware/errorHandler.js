const logger = require("../config/logger");


const errorHandler = (

    err,
    req,
    res,
    next

)=>{


    const statusCode =
        err.statusCode || 500;



    // Log complete error internally

    logger.error({

        message: err.message,

        stack: err.stack,

        url: req.originalUrl,

        method: req.method

    });



    const response = {

        success:false,

        message:
            err.message || 
            "Internal Server Error"

    };



    /*
        Hide stack traces in production
    */

    if(process.env.NODE_ENV !== "production"){

        response.stack =
            err.stack;

    }



    res.status(statusCode)
       .json(response);



};


module.exports = errorHandler;
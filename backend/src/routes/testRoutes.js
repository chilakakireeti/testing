const express = require("express");

const ApiError = require("../utils/ApiError");


const router = express.Router();



router.get(
    "/success",
    (req,res)=>{

        res.json({

            success:true,

            message:
            "API working"

        });

    }

);



router.get(
    "/error",
    (req,res,next)=>{


        next(

            new ApiError(
                400,
                "Example generated error"
            )

        );


    }

);



module.exports = router;
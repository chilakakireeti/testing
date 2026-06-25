import { Request, Response } from "express";


export const healthCheck = (
    req: Request,
    res: Response
) => {

    res.json({
        status: "success",
        message: "Backend is running"
    });

};
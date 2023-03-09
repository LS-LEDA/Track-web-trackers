import { RequestHandler } from 'express';

export const getTrackers: RequestHandler = async (req, res) => {
    const url = req.params.url;

    const { exec } = require('child_process');

    const trackers = await new Promise((resolve, reject) => {
        exec('python ../py_detector/py_detector.py https://' + url, (err: any, stdout: any, stderr: any) => {
            if (err) {
                console.log(err);
                resolve({ error: "Something went wrong. :/" });
                return;
            }

            console.log(`stderr: ${stderr}`);
            resolve(JSON.parse(stdout || "[]"));
        });

    });

    res.json(trackers);
}
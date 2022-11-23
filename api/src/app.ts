import express from 'express';
import morgan from 'morgan';
import cors from 'cors';

import entityRoutes from './routes/routes';
import dotenv from 'dotenv';

/** Reads .env from local file */
dotenv.config();
const app = express();

app.set("port", process.env.PORT || 3000);

app.use(morgan('dev'));
app.use(cors());
app.use(express.json({}));

app.use(entityRoutes);

export default app;
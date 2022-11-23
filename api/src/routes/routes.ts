import { Router } from 'express';
const router = Router();

import * as entityController from './controller';

router.get('/trackers/:url', entityController.getTrackers);

export default router;
import { validateUpload } from '../src/validateUpload';

const oneByteOverThreeMb = 3 * 1024 * 1024 + 1;
const result = validateUpload({ size: oneByteOverThreeMb, type: 'image/png' });

if (result !== 'file_too_large') throw new Error('Expected the implemented 3 MB limit.');

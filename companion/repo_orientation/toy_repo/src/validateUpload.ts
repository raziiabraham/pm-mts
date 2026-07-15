const MAX_UPLOAD_BYTES = 3 * 1024 * 1024;

export function validateUpload(file: { size: number; type: string }) {
  if (!['image/jpeg', 'image/png'].includes(file.type)) return 'unsupported_format';
  if (file.size > MAX_UPLOAD_BYTES) return 'file_too_large';
  return 'accepted';
}

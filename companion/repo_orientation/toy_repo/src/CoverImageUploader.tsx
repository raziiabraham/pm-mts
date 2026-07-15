export const uploadStates = [
  "select",
  "preview",
  "replace",
  "remove",
  "uploading",
  "saved",
  "error",
] as const;

export function uploadHelpText() {
  return "Choose a JPEG or PNG cover image.";
}

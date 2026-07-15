export function afterCoverSaved(documentId: string, sourceSurface: string) {
  return {
    eventName: 'Document Cover Updated',
    properties: { documentId, sourceSurface },
  };
}

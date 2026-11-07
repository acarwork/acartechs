const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('sayfaDesktop', {
  pickBooks: () => ipcRenderer.invoke('pick-books'),
  exportNotes: (data) => ipcRenderer.invoke('export-notes', data),
  openExternal: (url) => ipcRenderer.invoke('open-external', url),
  isDesktop: true
});

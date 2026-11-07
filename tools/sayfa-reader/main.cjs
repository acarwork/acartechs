const { app, BrowserWindow, dialog, ipcMain, shell, protocol } = require('electron');
const fs = require('node:fs/promises');
const path = require('node:path');

protocol.registerSchemesAsPrivileged([{ scheme: 'sayfa', privileges: { standard: true, secure: true, supportFetchAPI: true, corsEnabled: true } }]);

let win;
function createWindow() {
  win = new BrowserWindow({
    width: 1380, height: 900, minWidth: 860, minHeight: 620, fullscreenable: true,
    title: 'Sayfa — Kişisel Kitaplığın',
    backgroundColor: '#f7f4ed',
    webPreferences: { preload: path.join(__dirname, 'preload.cjs'), contextIsolation: true, nodeIntegration: false, sandbox: true }
  });
  win.loadURL('sayfa://app/reader.html');
}
app.whenReady().then(async () => {
  const mime = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.txt': 'text/plain; charset=utf-8' };
  await protocol.handle('sayfa', async request => {
    try {
      const url = new URL(request.url);
      const file = path.resolve(__dirname, `.${decodeURIComponent(url.pathname)}`);
      if (!file.startsWith(path.resolve(__dirname) + path.sep)) return new Response('Not found', { status: 404 });
      const data = await fs.readFile(file);
      return new Response(data, { headers: { 'content-type': mime[path.extname(file).toLowerCase()] || 'application/octet-stream' } });
    } catch { return new Response('Not found', { status: 404 }); }
  });
  createWindow();
  app.on('activate', () => { if (!BrowserWindow.getAllWindows().length) createWindow(); });
});
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });
ipcMain.handle('pick-books', async () => {
  const result = await dialog.showOpenDialog(win, {
    title: 'Kitap dosyası seç', properties: ['openFile', 'multiSelections'],
    filters: [{ name: 'E-kitap ve belge', extensions: ['pdf','epub','mobi','azw','azw3','fb2','cbz','cbr','txt','html','htm','xhtml','zip'] }]
  });
  if (result.canceled) return [];
  return Promise.all(result.filePaths.map(async filePath => {
    const stat = await fs.stat(filePath);
    return { name: path.basename(filePath), path: filePath, size: stat.size, url: require('node:url').pathToFileURL(filePath).href };
  }));
});
ipcMain.handle('export-notes', async (_event, { name, text }) => {
  const result = await dialog.showSaveDialog(win, { defaultPath: `${name}-notlar.txt`, filters: [{ name: 'Metin dosyası', extensions: ['txt'] }] });
  if (!result.canceled) await fs.writeFile(result.filePath, text, 'utf8');
  return !result.canceled;
});
ipcMain.handle('open-external', (_event, url) => shell.openExternal(url));

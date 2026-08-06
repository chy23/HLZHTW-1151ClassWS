import re

with open("src/components/HandoutViewer.jsx", "r", encoding="utf-8") as f:
    code = f.read()

# Replace the Tool Mode hook to include Canvas drawing states
tool_mode_setup = """  const [toolMode, setToolMode] = useState('none');
  const [exportSize, setExportSize] = useState('A4');
  const [exportMargin, setExportMargin] = useState('standard');
  const [zoomLevel, setZoomLevel] = useState(1);
  const [isWidescreen, setIsWidescreen] = useState(false);
  
  // 畫布狀態
  const [paths, setPaths] = useState([]);
  const [currentPath, setCurrentPath] = useState(null);"""

code = code.replace(
    "  const [toolMode, setToolMode] = useState('none');\n  const [exportSize, setExportSize] = useState('A4');\n  const [exportMargin, setExportMargin] = useState('standard');\n  const [zoomLevel, setZoomLevel] = useState(1);\n  const [isWidescreen, setIsWidescreen] = useState(false);",
    tool_mode_setup
)

# Update control bar
old_controls = """        <div className="flex gap-3 flex-wrap justify-center items-center">
          {/* 版權註記 */}
          <div className="text-[11px] text-amber-700 bg-amber-50 border border-amber-200 p-1.5 rounded text-right leading-tight mr-1 hidden md:block">
            學習單資料取自「翰林出版社」<br/>
            網站內容僅限用於孩子學習使用<br/>
            <span className="text-red-600 font-bold">切勿用於商業行為</span>
          </div>
          {/* 縮放 */}
          <div className="flex items-center gap-1 bg-slate-100 dark:bg-slate-700 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700">
            <button onClick={() => setZoomLevel(z => Math.max(0.5, parseFloat((z - 0.1).toFixed(1))))} className="p-1 hover:bg-white dark:bg-slate-800 rounded text-slate-600 dark:text-slate-300 dark:text-slate-600" title="縮小"><ZoomOut size={18} /></button>
            <span className="text-sm font-bold w-12 text-center text-slate-700 dark:text-slate-300 dark:text-slate-600">{Math.round(zoomLevel * 100)}%</span>
            <button onClick={() => setZoomLevel(z => Math.min(2, parseFloat((z + 0.1).toFixed(1))))} className="p-1 hover:bg-white dark:bg-slate-800 rounded text-slate-600 dark:text-slate-300 dark:text-slate-600" title="放大"><ZoomIn size={18} /></button>
          </div>
          {/* 拉寬 */}
          <button onClick={() => setIsWidescreen(!isWidescreen)} className={`px-3 py-1.5 rounded-lg text-sm font-bold border transition-colors ${isWidescreen ? 'bg-indigo-100 text-indigo-700 border-indigo-200' : 'bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 dark:text-slate-600 border-slate-200 dark:border-slate-700'}`}>
            {isWidescreen ? '縮回版面' : '拉寬版面'}
          </button>
          {/* 版面設定 */}
          <div className="flex items-center gap-3 bg-slate-100 dark:bg-slate-700 px-4 py-2 rounded-lg border border-slate-200 dark:border-slate-700">
            <label className="text-sm font-bold text-slate-700 dark:text-slate-300 dark:text-slate-600 flex items-center">版面：
              <select className="ml-1 border-slate-300 rounded text-sm p-1" value={exportSize} onChange={e => setExportSize(e.target.value)}>
                <option value="A4">A4</option><option value="B4">B4</option><option value="A3">A3</option>
              </select>
            </label>
            <label className="text-sm font-bold text-slate-700 dark:text-slate-300 dark:text-slate-600 flex items-center">邊界：
              <select className="ml-1 border-slate-300 rounded text-sm p-1" value={exportMargin} onChange={e => setExportMargin(e.target.value)}>
                <option value="standard">標準</option><option value="wide">寬</option><option value="narrow">窄</option>
              </select>
            </label>
          </div>
          <button onClick={toggleShowAll} className="bg-blue-100 hover:bg-blue-200 text-blue-800 px-4 py-2 rounded-lg font-bold shadow-sm transition-colors text-sm">
            {showAllAnswers ? '🔒 隱藏全解答' : '👁️ 顯示全解答'}
          </button>
          <button onClick={() => exportToWord('teacher')} className="bg-teal-600 hover:bg-teal-700 text-white px-4 py-2 rounded-lg shadow font-bold text-sm">匯出教用版</button>
          <button onClick={() => exportToWord('student')} className="bg-amber-500 hover:bg-amber-600 text-white px-4 py-2 rounded-lg shadow font-bold text-sm">匯出學用版</button>
        </div>"""

new_controls = """        <div className="flex gap-3 flex-wrap justify-center items-center">
          {/* 深色模式與全解答 */}
          <div className="flex bg-slate-100 dark:bg-slate-700 rounded-lg p-1 border border-slate-200 dark:border-slate-600 shadow-sm">
            <button onClick={() => setIsDarkMode(!isDarkMode)} className={`p-1.5 rounded-md transition-colors ${isDarkMode ? 'text-amber-400 bg-slate-800' : 'text-slate-500 hover:bg-slate-200'}`} title="深色模式切換">
              {isDarkMode ? <Moon size={18} /> : <Sun size={18} />}
            </button>
            <div className="w-px bg-slate-300 dark:bg-slate-600 mx-1 my-1"></div>
            <button onClick={toggleShowAll} className={`flex items-center gap-1 px-3 py-1.5 rounded-md text-sm font-bold transition-colors ${showAllAnswers ? 'bg-blue-100 text-blue-700 dark:bg-blue-900/50 dark:text-blue-300' : 'text-slate-600 hover:bg-slate-200 dark:text-slate-300 dark:hover:bg-slate-600'}`}>
              {showAllAnswers ? <><EyeOff size={16}/> 隱藏解答</> : <><Eye size={16}/> 顯示全解答</>}
            </button>
          </div>

          {/* 字體大小 */}
          <div className="flex items-center bg-slate-100 dark:bg-slate-700 rounded-lg border border-slate-200 dark:border-slate-700 overflow-hidden shadow-sm">
            <button onClick={() => setZoomLevel(0.8)} className={`px-3 py-1.5 text-sm font-bold transition-colors ${zoomLevel === 0.8 ? 'bg-blue-500 text-white' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-600'}`}>A-</button>
            <button onClick={() => setZoomLevel(1)} className={`px-3 py-1.5 text-sm font-bold transition-colors border-x border-slate-200 dark:border-slate-600 ${zoomLevel === 1 ? 'bg-blue-500 text-white' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-600'}`}>A</button>
            <button onClick={() => setZoomLevel(1.3)} className={`px-3 py-1.5 text-sm font-bold transition-colors ${zoomLevel === 1.3 ? 'bg-blue-500 text-white' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-600'}`}>A+</button>
          </div>

          {/* 拉寬版面 */}
          <button onClick={() => setIsWidescreen(!isWidescreen)} className={`px-3 py-1.5 rounded-lg text-sm font-bold border transition-colors shadow-sm ${isWidescreen ? 'bg-indigo-100 text-indigo-700 border-indigo-200 dark:bg-indigo-900/40 dark:text-indigo-300 dark:border-indigo-800' : 'bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700 hover:bg-slate-200 dark:hover:bg-slate-600'}`}>
            {isWidescreen ? '縮回版面' : '拉寬版面'}
          </button>

          {/* 匯出區塊 (隱藏細節版面設定以簡化介面，預設為A4標準) */}
          <div className="flex rounded-lg overflow-hidden border border-slate-200 dark:border-slate-700 shadow-sm">
            <button onClick={() => exportToWord('teacher')} className="bg-teal-600 hover:bg-teal-700 text-white px-3 py-1.5 font-bold text-sm">匯出教用版</button>
            <button onClick={() => exportToWord('student')} className="bg-amber-500 hover:bg-amber-600 text-white px-3 py-1.5 font-bold text-sm">匯出學用版</button>
          </div>
        </div>"""

code = code.replace(old_controls, new_controls)

# SVG Canvas overlay inside #printable-area
canvas_handlers = """
  // 畫布事件處理
  const handlePointerDown = (e) => {
    if (toolMode !== 'draw') return;
    const rect = e.currentTarget.getBoundingClientRect();
    const x = (e.clientX - rect.left) / zoomLevel;
    const y = (e.clientY - rect.top) / zoomLevel;
    setCurrentPath(`M ${x} ${y}`);
  };

  const handlePointerMove = (e) => {
    if (toolMode !== 'draw' || !currentPath) return;
    const rect = e.currentTarget.getBoundingClientRect();
    const x = (e.clientX - rect.left) / zoomLevel;
    const y = (e.clientY - rect.top) / zoomLevel;
    setCurrentPath(prev => `${prev} L ${x} ${y}`);
  };

  const handlePointerUp = () => {
    if (toolMode !== 'draw' || !currentPath) return;
    setPaths(prev => [...prev, currentPath]);
    setCurrentPath(null);
  };
"""

# Insert right after useEffect(() => { document.body.className = ... })
code = code.replace(
    "  }, [toolMode]);\n\n  const clearAllHighlight = () => {",
    "  }, [toolMode]);\n" + canvas_handlers + "\n  const clearAllHighlight = () => {\n    setPaths([]);"
)

printable_area_start = """          id="printable-area"
          className={`relative w-full ${isWidescreen ? 'max-w-[1200px]' : 'max-w-[850px]'} bg-white dark:bg-slate-800 p-10 md:p-16 shadow-xl rounded-xl border border-slate-100 dark:border-slate-700 content-area self-start`}
          style={{ zoom: zoomLevel }}
        >"""

printable_area_with_canvas = printable_area_start + """
          {/* 畫布層 (絕對定位覆蓋整個區域) */}
          <svg 
            className={`absolute inset-0 w-full h-full z-30 pointer-events-${toolMode === 'draw' ? 'auto' : 'none'} no-print`}
            onPointerDown={handlePointerDown}
            onPointerMove={handlePointerMove}
            onPointerUp={handlePointerUp}
            onPointerLeave={handlePointerUp}
          >
            {paths.map((p, i) => (
              <path key={i} d={p} stroke="red" strokeWidth="3" fill="none" strokeLinecap="round" strokeLinejoin="round" />
            ))}
            {currentPath && (
              <path d={currentPath} stroke="red" strokeWidth="3" fill="none" strokeLinecap="round" strokeLinejoin="round" />
            )}
          </svg>"""

code = code.replace(printable_area_start, printable_area_with_canvas)

# Add Draw Tool to floating toolbar
floating_tools_old = """      {/* 浮動工具列 */}
      <div className="no-print fixed bottom-8 right-8 bg-white dark:bg-slate-800/90 backdrop-blur-md p-3 rounded-full shadow-2xl border border-slate-200 dark:border-slate-700 flex flex-col space-y-3 z-50">
        <button onClick={() => setToolMode(toolMode === 'pen' ? 'none' : 'pen')} className={`p-4 rounded-full transition-all ${toolMode === 'pen' ? 'bg-yellow-300 text-yellow-800 shadow-inner' : 'bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:bg-slate-600 text-slate-600 dark:text-slate-300 dark:text-slate-600'}`} title="螢光筆畫記 (選取文字來畫記)"><PenTool size={24} /></button>
        <button onClick={() => setToolMode(toolMode === 'eraser' ? 'none' : 'eraser')} className={`p-4 rounded-full transition-all ${toolMode === 'eraser' ? 'bg-pink-300 text-pink-800 shadow-inner' : 'bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:bg-slate-600 text-slate-600 dark:text-slate-300 dark:text-slate-600'}`} title="橡皮擦 (點擊螢光筆，或選取文字來擦除)"><Eraser size={24} /></button>
        <button onClick={clearAllHighlight} className="p-4 rounded-full bg-slate-100 dark:bg-slate-700 hover:bg-red-100 hover:text-red-600 text-slate-600 dark:text-slate-300 dark:text-slate-600 transition-colors" title="清除所有畫記"><Trash2 size={24} /></button>
      </div>"""

floating_tools_new = """      {/* 浮動工具列 */}
      <div className="no-print fixed bottom-8 right-8 bg-white dark:bg-slate-800/90 backdrop-blur-md p-3 rounded-full shadow-2xl border border-slate-200 dark:border-slate-700 flex flex-col space-y-3 z-50">
        <button onClick={() => setToolMode(toolMode === 'draw' ? 'none' : 'draw')} className={`p-4 rounded-full transition-all ${toolMode === 'draw' ? 'bg-red-500 text-white shadow-inner' : 'bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:bg-slate-600 text-slate-600 dark:text-slate-300'}`} title="自由手繪 (直接在講義上畫線)"><Brush size={24} /></button>
        <button onClick={() => setToolMode(toolMode === 'pen' ? 'none' : 'pen')} className={`p-4 rounded-full transition-all ${toolMode === 'pen' ? 'bg-yellow-300 text-yellow-800 shadow-inner' : 'bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:bg-slate-600 text-slate-600 dark:text-slate-300'}`} title="螢光筆畫記 (選取文字來畫記)"><PenTool size={24} /></button>
        <button onClick={() => setToolMode(toolMode === 'eraser' ? 'none' : 'eraser')} className={`p-4 rounded-full transition-all ${toolMode === 'eraser' ? 'bg-pink-300 text-pink-800 shadow-inner' : 'bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:bg-slate-600 text-slate-600 dark:text-slate-300'}`} title="橡皮擦 (點擊螢光筆，或選取文字來擦除)"><Eraser size={24} /></button>
        <div className="w-full h-px bg-slate-200 dark:bg-slate-600"></div>
        <button onClick={clearAllHighlight} className="p-4 rounded-full bg-slate-100 dark:bg-slate-700 hover:bg-red-100 dark:hover:bg-red-900/50 hover:text-red-600 dark:hover:text-red-400 text-slate-600 dark:text-slate-300 transition-colors" title="清除所有畫記與手繪"><Trash2 size={24} /></button>
      </div>"""

code = code.replace(floating_tools_old, floating_tools_new)

# Add HandoutViewer isDarkMode props destructuring
code = code.replace(
    "export default function HandoutViewer({ lesson, isSidebarOpen, setIsSidebarOpen }) {",
    "export default function HandoutViewer({ lesson, isSidebarOpen, setIsSidebarOpen, isDarkMode, setIsDarkMode }) {"
)

with open("src/components/HandoutViewer.jsx", "w", encoding="utf-8") as f:
    f.write(code)

print("Update Complete")

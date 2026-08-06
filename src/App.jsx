import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import HandoutViewer from './components/HandoutViewer';

// 自訂 Hook：用於 localStorage
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });

  const setValue = (value) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };
  return [storedValue, setValue];
}

function App() {
  const [lessons, setLessons] = useState([]);
  const [currentLessonId, setCurrentLessonId] = useLocalStorage('hlzhtw_current_lesson', null);
  const [currentLessonData, setCurrentLessonData] = useState(null);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [isLoading, setIsLoading] = useState(true);
  
  // 深色模式狀態
  const [isDarkMode, setIsDarkMode] = useLocalStorage('hlzhtw_dark_mode', false);

  // 初始化深色模式
  useEffect(() => {
    if (isDarkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDarkMode]);

  // 載入課程目錄 (Lazy Loading 步驟 1)
  useEffect(() => {
    fetch(`${import.meta.env.BASE_URL}data/lessons_index.json`)
      .then(res => res.json())
      .then(data => {
        setLessons(data);
        // 如果沒有選定課文，或選定的課文不在目錄中，則預設為第一課
        const storedId = JSON.parse(window.localStorage.getItem('hlzhtw_current_lesson') || 'null');
        if (data.length > 0 && (!storedId || !data.find(l => l.id === storedId))) {
          setCurrentLessonId(data[0].id);
        }
      })
      .catch(err => console.error("無法載入課程目錄:", err));
  }, []);

  // 載入單一課文內容 (Lazy Loading 步驟 2)
  useEffect(() => {
    if (!currentLessonId) return;
    setIsLoading(true);
    fetch(`${import.meta.env.BASE_URL}data/${currentLessonId}.json`)
      .then(res => res.json())
      .then(data => {
        setCurrentLessonData(data);
        setIsLoading(false);
      })
      .catch(err => {
        console.error("無法載入課文資料:", err);
        setIsLoading(false);
      });
  }, [currentLessonId]);

  return (
    <div className={`flex h-screen overflow-hidden bg-slate-50 dark:bg-slate-900 selection:bg-blue-100 dark:selection:bg-blue-900 relative transition-colors duration-300`}>
      {/* Background Decor */}
      <div className="fixed inset-0 pointer-events-none no-print overflow-hidden">
        <div className="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] rounded-full bg-blue-100/40 dark:bg-blue-900/20 blur-3xl transition-colors duration-300" />
        <div className="absolute bottom-[-20%] right-[-10%] w-[50%] h-[50%] rounded-full bg-teal-100/40 dark:bg-teal-900/20 blur-3xl transition-colors duration-300" />
      </div>

      {/* 手機版側邊欄遮罩 (Overlay) */}
      {isSidebarOpen && (
        <div 
          className="fixed inset-0 bg-black/50 z-40 md:hidden backdrop-blur-sm transition-opacity no-print" 
          onClick={() => setIsSidebarOpen(false)}
        />
      )}

      {/* 固定浮水印 */}
      <div className="fixed top-[100px] right-8 z-50 pointer-events-none select-none no-print text-slate-500/25 dark:text-slate-400/20 text-[18pt] font-bold tracking-widest">
        網站建立自楊家驊老師
      </div>
      <div className="fixed bottom-8 right-28 z-50 pointer-events-none select-none no-print text-slate-500/25 dark:text-slate-400/20 text-[18pt] font-bold tracking-widest">
        網站建立自楊家驊老師
      </div>

      <Sidebar
        lessons={lessons}
        currentLessonId={currentLessonId}
        onSelectLesson={setCurrentLessonId}
        isOpen={isSidebarOpen}
        setIsOpen={setIsSidebarOpen}
      />

      <main className="flex-1 h-screen overflow-y-auto relative z-10 no-scrollbar">
        {isLoading ? (
          <div className="flex items-center justify-center h-full text-slate-500 dark:text-slate-400 font-medium text-lg">
            載入中...
          </div>
        ) : currentLessonData ? (
          <HandoutViewer 
            lesson={currentLessonData} 
            isSidebarOpen={isSidebarOpen} 
            setIsSidebarOpen={setIsSidebarOpen} 
            isDarkMode={isDarkMode}
            setIsDarkMode={setIsDarkMode}
          />
        ) : (
          <div className="flex items-center justify-center h-full text-slate-500 dark:text-slate-400 font-medium text-lg">
            請從左側選單選擇一課開始
          </div>
        )}
      </main>
    </div>
  );
}

export default App;

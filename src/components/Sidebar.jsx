import React from 'react';
import { BookOpen, ChevronRight, ChevronLeft } from 'lucide-react';

export default function Sidebar({ lessons, currentLessonId, onSelectLesson, isOpen, setIsOpen }) {
  return (
    <div className={`bg-white/60 dark:bg-slate-900/80 backdrop-blur-xl border-slate-200 dark:border-slate-800 h-screen overflow-hidden flex flex-col no-print sticky top-0 shadow-lg shrink-0 transition-all duration-300 ease-in-out ${isOpen ? 'w-72 border-r' : 'w-0 border-r-0'}`}>
      <div className="w-72 flex flex-col h-full overflow-y-auto">
        <div className="p-6 border-b border-slate-200/50 dark:border-slate-700/50 flex justify-between items-center shrink-0">
          <div className="flex items-center gap-3">
            <div className="bg-blue-600 dark:bg-blue-500 text-white p-2 rounded-xl shadow-md shadow-blue-600/20 dark:shadow-blue-900/40">
              <BookOpen size={24} />
            </div>
            <div>
              <h1 className="text-xl font-extrabold text-slate-800 dark:text-slate-100 tracking-tight">國語學習單平台</h1>
              <p className="text-xs text-slate-500 dark:text-slate-400 font-medium mt-0.5">專屬高效學習系統</p>
            </div>
          </div>
          <button onClick={() => setIsOpen(false)} className="text-slate-400 dark:text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 p-1.5 rounded-full transition-colors" title="收折側邊欄">
            <ChevronLeft size={20} />
          </button>
        </div>

        <div className="flex-1 p-4 space-y-2">
          <h2 className="text-xs font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-4 px-2">課程列表</h2>
          {lessons.map((lesson) => {
            const isActive = currentLessonId === lesson.id;
            return (
              <button
                key={lesson.id}
                onClick={() => onSelectLesson(lesson.id)}
                className={`w-full flex items-center justify-between p-3 rounded-xl transition-all duration-200 group ${
                  isActive
                    ? 'bg-blue-50 dark:bg-blue-900/30 border border-blue-100 dark:border-blue-800 shadow-sm'
                    : 'hover:bg-slate-50 dark:hover:bg-slate-800/50 border border-transparent'
                }`}
              >
                <div className="flex flex-col items-start text-left">
                  <span className={`text-xs font-bold ${isActive ? 'text-blue-600 dark:text-blue-400' : 'text-slate-500 dark:text-slate-400 group-hover:text-slate-700 dark:group-hover:text-slate-300'}`}>
                    {lesson.lessonNum}
                  </span>
                  <span className={`text-sm font-bold mt-0.5 ${isActive ? 'text-blue-900 dark:text-blue-100' : 'text-slate-700 dark:text-slate-300 group-hover:text-slate-900 dark:group-hover:text-slate-100'}`}>
                    {lesson.lessonName}
                  </span>
                </div>
                <ChevronRight
                  size={16}
                  className={`transition-transform duration-200 ${isActive ? 'text-blue-600 dark:text-blue-400 translate-x-1' : 'text-slate-300 dark:text-slate-600 opacity-0 group-hover:opacity-100 group-hover:translate-x-0 -translate-x-2'}`}
                />
              </button>
            );
          })}
        </div>

        <div className="p-6 border-t border-slate-200/50 dark:border-slate-700/50 bg-slate-50/50 dark:bg-slate-900/50 mt-auto shrink-0">
          <div className="text-xs text-slate-400 dark:text-slate-500 text-center font-medium">
            系統更新：每週上架新課文
          </div>
        </div>
      </div>
    </div>
  );
}

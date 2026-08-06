import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({ error, errorInfo });
    console.error("ErrorBoundary caught an error", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: '20px', background: '#ffebee', color: '#c62828', height: '100vh', overflow: 'auto' }}>
          <h2>網頁發生錯誤 (Error Boundary)</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            <summary>點擊查看錯誤細節</summary>
            {this.state.error && this.state.error.toString()}
            <br />
            {this.state.errorInfo && this.state.errorInfo.componentStack}
          </details>
          <button onClick={() => { window.localStorage.clear(); window.location.reload(); }} style={{ marginTop: '20px', padding: '10px', background: '#c62828', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>
            清除快取並重新整理
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}

export default ErrorBoundary;

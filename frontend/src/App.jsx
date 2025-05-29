import React from "react"
import Index from "./pages/Index"
import Header from "./components/Header"
function App() {

  return (
    <>

      <div className='w-full h-screen flex flex-col justify-center items-center'>
        <Header/>
        <Index/>
      </div>
    </>
  )
}

export default App

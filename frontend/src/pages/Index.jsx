import React from "react"
import Mapa from "../components/Map"

function Index() {

  return (
    <>
        <div className="flex flex-col items-center h-full w-full">
            <h1 className='font-bold text-3xl mb-3'>Será que vem chuva por aí?</h1>
            <form action="" className='w-full flex justify-center'>
                <input
                type="text"
                id='cidadeTxt'
                placeholder='Digite a sua cidade e descubra'
                className='border-2 rounded-full p-4 w-1/2 mb-3 text-xl transition-all ease-in-out 
                            focus:outline-none focus:scale-103 focus:bg-white/10
                            hover:scale-103 hover:bg-white/10 font-extralight' 
                />
            </form>
            <p className='text-2xl text-center font-medium'>
            Ou <br />selecione a sua zona no mapa e nós tratamos do resto!
            </p>
            <div className='w-2/4 h-3/6 border-2 mt-4 rounded-lg shadow-lg transition-all ease-in-out hover:scale-108 '>
                <Mapa />
            </div>
        </div>
    </>
  )
}

export default Index

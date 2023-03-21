function sort(){
    let numero=Number(window.prompt('Digite um número: '))
    let reverso= numero.toString().split('').reverse().join()

    let res=document.querySelector('section#saida')
    res.innerHTML=`<p> O numero reverso é ${reverso}`
}
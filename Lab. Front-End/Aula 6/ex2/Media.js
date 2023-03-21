function media(){
    let n1=Number(window.prompt('Digite uma número: '))
    let n2=Number(window.prompt('Digite uma número: '))
    
    let soma= n1+n2
    let media= soma/2
    let res=document.querySelector('section#saida')
    res.innerHTML=`<p> A media dos 2 numeros é ${media}`
}
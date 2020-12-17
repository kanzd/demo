
var compile = async (code,input)=>{
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code:code,input:input })
    };
   var response = await  fetch('http://127.0.0.1:8000/code/', requestOptions);
    return response;
}

export default compile;
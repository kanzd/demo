import React,{Component} from 'react';
import '../css/code.css';
import Input from "./Input";
import Output from './output';
import compile from '../services/compile';

class Root extends Component
{
    state = {
        input:"",
        output:'',
        code :"",
    }

    render()
    {
        return (

            <div className="form-floating">

<div className="input-group ">
  <span className="input-group-text">Write Your Code</span>
  <textarea className="form-control container" id = 'code' aria-label="With textarea"></textarea>
</div>
  <Input />
  <button type="button" className="btn btn-info code" onClick={
    (e)=>
    {
    var code=document.getElementById('code').value;
    var input = document.getElementById('input').value;
    console.log(code);
    console.log(input);
    (async()=>{
      var output=await compile(code,input);
   console.log(output);
   var i = await output.json();
   console.log(i.output);
   var final = i.output.substring(2);

   
   
   this.setState({output:final});

   
      
    })();
    

    }
  }>Compile</button>
  <Output output={this.state.output} />
</div>
        );
    }

}

export default Root
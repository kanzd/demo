import React,{Component} from 'react';


class Output extends Component
{
    state = {
        output:"",
    }
    render()
    {
        return (
            <div className="card">
  <div className="card-body">
   {this.props.output}
  </div>
</div>

        );
    }
}

export default Output
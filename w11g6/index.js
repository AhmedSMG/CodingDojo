const abi = ""; // The ABI of the contract
const contractAddress = ""; // Address of the deployed contract
let account;

function main(){

    if (!ethereum.isMetaMask || !window.ethereum.isMetaMask){
        throw new Error("Please install MetaMask");
    }
    ethereum.request({method: "eth_requestAccounts"});
    console.log("Hi")
    const web3 = new Web3(window.ethereum);
    f();
}

async function f(){
    account = await web3.eth.getAccounts()[0];
    alert(`Account: ${account}`)
    const contract = await new web3.eth.Contract(abi, contractAddress); // get the deplyed contract


    const defualtMessage = await contract.methods.getMessage().call(); //get the defualt message
    alert(`Origional: ${defualtMessage}`);
    
    const newMessage = ""// new message to set
    await contract.methods.setMessage(newMessage);

    const updatedMessgae = await contract.methods.getMessage().call(); //get the defualt message
    alert(`Updated: ${updatedMessgae}`);
}

main();
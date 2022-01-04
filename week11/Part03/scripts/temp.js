function main(){
    f();
}

async function f(){
    const accounts = await web3.eth.getAccounts()[0];
    const balance = await web3.eth.getBalance(account);

    const contract = await new web3.eth.Contract(abi)
    .deploy({data: bytecode, arguments: []})
    .send({from: account, gas: "1000000"});

    console.log(contract);

    const initMessage = await contract.methods.getSecret().call({from: account});
    const resp = await contract.methods.setSecret(newMessage).send({from: account, gas: "100000"});


}
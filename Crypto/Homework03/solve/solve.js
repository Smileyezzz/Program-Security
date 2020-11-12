const fs = require('fs')
const lib = require('./lib')(require('./config'))

web3 = lib.web3

async function main () {
    let factory_address = '0x8e0a809B1f413deB6427535cC53383954DBF8329'
    let factory = lib.contract(factory_address, JSON.parse(fs.readFileSync('BetFactory.abi')))
    let cake_address = '...' //Here is your deployed contract address
    let cake = lib.contract(cake_address, JSON.parse(fs.readFileSync('Cake.abi')))
    let instance_address = await factory.view('instances', cake_address)
    if (instance_address === '0x0000000000000000000000000000000000000000') {
        await cake.call({value: web3.utils.toWei('0.5', 'ether')}, 'create', factory_address)
        instance_address = await factory.view('instances', cake_address)
    }
    await cake.call({value: web3.utils.toWei('0.5', 'ether')}, 'run', instance_address)
}

main()



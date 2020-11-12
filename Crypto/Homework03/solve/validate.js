const fs = require('fs')
const lib = require('./lib')(require('./config'))

async function main () {
    let cake_address = '...' // Here is your deployed contract address
    let validate_token = '...' // Here is token produed by server.py
    let cake = lib.contract(cake_address, JSON.parse(fs.readFileSync('Cake.abi')))
    await cake.call('validate', '0x8e0a809B1f413deB6427535cC53383954DBF8329', validate_token)
}

main()

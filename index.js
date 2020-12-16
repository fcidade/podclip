const readline = require('readline-sync')

function start() {
  const content = {}
  content.searchTerm = askAndReturnSearchTerm()
  content.prefix = askAndReturnPrefix(content.searchTerm)

  function askAndReturnSearchTerm() {
    return readline.question('Type a Wikipedia search term: ')
  }

  function askAndReturnPrefix(searchTerm) {
    const prefixes = ['Who is', 'What is', 'The history of']
    const selectedPrefixIndex = readline.keyInSelect(prefixes, `Select a prefix for ${searchTerm}:`)
    return prefixes[selectedPrefixIndex]
  }

  console.log(content)
}

start()
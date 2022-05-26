const palindromeVerifier = (str) => {
    const strReversed = str.split("").reverse().join("");
  
    return strReversed === str ? "es palindromo" : "no es palindromo";
  }
  console.log(palindromeVerifier("owo")); 
  console.log(palindromeVerifier("enroute")); 
  console.log(palindromeVerifier("anitalavalatina")); 
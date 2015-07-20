#From http://www.codewars.com/kata/514a024011ea4fb54200004b

#Description:

#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

#domain_name("http://github.com/carbonfive/raygun") == "github" 
#domain_name("http://www.zombie-bites.com") == "zombie-bites"
#domain_name("https://www.cnet.com") == "cnet"

def domain_name(url)
  # since potential subdomains must come prior to the domain name,
  # reading after reversed URL's first period will give us the domain name
  url.reverse.match(/\.[\w-]+(\/|\.)/)[0].reverse[1..-2]
end

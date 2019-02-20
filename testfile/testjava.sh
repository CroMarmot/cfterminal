mkdir -p TEST
file="$1".java
if [ -f "$file" ]
then
  cp "$file" TEST/Main.java && cd TEST && javac Main.java && java -Xmx512M -Xss64M Main && cd ..
else
  echo "$file not found."
fi

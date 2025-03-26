
# Use the official Node.js image to build React app
FROM node:16-alpine as build

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the source code
COPY . .

# Build the React app
RUN npm run build

# Stage for running the app
FROM nginx:alpine

# Copy the built React app to NGINX's public directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for the frontend
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

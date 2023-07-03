# Use the official Node.js base image from Docker Hub
FROM node:16-alpine as base

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and pnpm-lock.yaml files into the container
COPY package.json pnpm-lock.yaml ./

# Install PNPM package manager globally
RUN npm install -g pnpm

# Install project dependencies using PNPM
RUN pnpm install --frozen-lockfile

# Build the Next.js app
RUN pnpm build

# Use the official Nginx base image from Docker Hub
FROM nginx:alpine

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the built application from the builder stage to the Nginx web root directory
COPY --from=base /app/.next /usr/share/nginx/html

# Expose the port that Nginx will be listening on
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

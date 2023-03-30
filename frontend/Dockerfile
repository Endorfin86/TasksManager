# Используем официальный образ Node.js в качестве базового образа
FROM node:14-alpine

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем package.json и package-lock.json в /app
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальные файлы в /app
COPY . .

# Собираем приложение
RUN npm run build

# Устанавливаем serve для запуска приложения
RUN npm install -g serve

# Открываем порт 80
EXPOSE 80

# Запускаем приложение
CMD ["serve", "-s", "dist", "-l", "80"]
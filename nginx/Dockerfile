FROM nginx

#RUN rm /etc/nginx/conf.d/default.conf

#COPY nginx.conf /etc/nginx/conf.d/

#RUN rm /etc/nginx/default.conf

COPY nginx.conf /etc/nginx

CMD ["nginx", "-g", "daemon off;"]
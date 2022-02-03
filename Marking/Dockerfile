FROM public.ecr.aws/lambda/python:3.9

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" && \
yum install -y mesa-libGL && \
cp /usr/lib64/libGL.so.1 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libGL.so.1.7.0 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libgthread-2.0.so.0 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libgthread-2.0.so.0 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libglib-2.0.so.0 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libGLX.so.0 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libX11.so.6 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libXext.so.6 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libGLdispatch.so.0 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libGLX_mesa.so.0.0.0 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libxcb.so.1 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libXau.so.6 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /usr/lib64/libXau.so.6 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
cp /lib64/libGLdispatch.so.0.0.0 ${LAMBDA_TASK_ROOT}/opencv_python.libs/ && \
rm -Rf ${LAMBDA_TASK_ROOT}/*.dist-info && \
yum remove -y mesa-libGL

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.lambda_handler" ]
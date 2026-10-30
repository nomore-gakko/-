import cv2
import numpy as np
from loguru import logger

logger.info("OpenCV 版本: {}", cv2.__version__)
logger.info("Numpy 版本: {}", np.__version__)

# 用 Numpy 创建一个纯黑图片
img = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.imshow("Test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
logger.success("环境完美！可以开始做任务啦！")

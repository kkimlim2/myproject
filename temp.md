## **ImageNet Classification with Deep Neural Networks**

 알렉스 넷은 ImageNet LSVRC-2010이라는 이미지 분류 대회에서 획기적으로 오류율을 낮춰 모두의 주목을 받았던 모델이다. 딥러닝을 성공적으로 활용했다고 평가받는 알렉스 넷에 대해서 ~며칠동안... 계속 봐서 쭈글쭈글 해진~ 공부한 내용을 포스팅 하도록 하겠다..

 논문 제목을 검색하면 바로 볼 수 있다.

 본 논문이 나온 시점은 바야흐로 2012년.. 초5 무렵이다

###  # 1. Introduction

  (논문 전체의 요약을 담고 있다 보통 서론은 그렇게 안 쓰지 않나?)

 많은 고해상도 이미지를 분류하기 위해서는 그만큼 큰 학습을 수용할 수 있는 모델이 필요함= > 그래서 CNN 활용함

($\\because$ 앞 포스팅에서도 말했듯이, CNN에서는 이미지의 공간적 정보를 학습하기 위해서 kernel을 이용함 그렇기 때문에 합성곱 층에서 사용하는 가중치의 갯수는 커널의 크기로 고정되어 있고, 그 크기는 사용자가 설정할 수 있음. 만약 그렇지 않고 그냥 다층 퍼셉트론을 사용한다면 input size \* hidden layer 의 계산결과 만큼 가중치가 필요함) 

[##_Image|kage@oSSwP/btq4c2ngIG3/xKLeHwfZEcXRCDxISji010/img.png|alignCenter|data-origin-width="835" data-origin-height="280" data-ke-mobilestyle="widthContent"|전 포스팅 그림을 훔쳐왔다||_##]

 거기에 더불어서, 몇가지 알렉스 넷에서는 성능을 높이고 학습 시간을 줄이기 위해서 '새롭고 특이한 기법 new and unusual features)' 과 과적합 방지를 위해서 '효과적인 기법effective techniques'을 사용했다. 자세한 건 section 3와 4에서 다룬다. 

 또, 현재 사용하고 있는 GPU는 GTX 580 3GV GPUs 라고 한다. 현재는 이것보다 더 발달된 GPU가 많아서, 실제로 이 알렉스넷에 사용됐던 몇 기법들은 안 쓴다고 한다.. 

 GPU, CPU 의 차이로는 GPU는 단순 계산에 적합하다고만 알면 될 것 같다. CPU는 보다 복잡한 계산에.

 구조를 미리 알면 나중에 볼 때 유용할 것 같아서 나중에 나오는 figure지만 미리 올린다. 

[##_Image|kage@mirJt/btq4cGY4BO5/G6qYaA8lGzYsv3FJ3GwyEk/img.png|alignCenter|data-origin-width="679" data-origin-height="228" width="820" height="NaN" data-ke-mobilestyle="widthContent"|ImageNet Classification with Deep Neural Networks Figure 2||_##]

###  # 2. The Dataset

 엄층 크다.

 15 million으이 고해상도 이미지, 총 22, 000 종류의 레이블이 있다. 엄청 크다. 근데 또 뻘한 웃긴 포인트는 이걸 다 사람이 수집하고 사람이 다 레이블 했다는 거다. ~수고하셨어요 아마존 직원분들... ~

그런데 문제는, 사람이 모은 데이터 셋의 이미지들이 그 규격이 모두 다르다는 것이다. 그래서 이미지 크기를 일정하게 맞추기 위해서, 사진 크기를 256 \* 256 으로 줄이는 down-sampled 했다고 한다. ~여러 포스팅을 참고했을 때, 다들 똑같은 그림을 쓰길래 대체 어디서 가지고 온걸까 싶은 의문이 들었지만...~ 

 일단 과정은 아래와 같다.

 - rescaled the image such that the shorter side was of length 256 짧은 변이 256이 되게끔 재조정? rescale한 후에

 - cropped out the central 256\*256 중앙을 잘라 256 \* 256을 만들었다. 

 내가 이해한 바로는 이런 과정을 겪을 것이고,

[##_Image|kage@cbHuec/btq4eibMNOu/oVGekCBFqKlURD9UXqviqk/img.png|alignCenter|width="762" height="182" data-origin-width="762" data-origin-height="182" data-ke-mobilestyle="widthContent"|||_##]

 정확한 이미지로는 아래와 같다. 보면 일단 이미지 사이즈가 비례해서 줄어들었고, 중간 부분만 잘린 것을 알 수 있다. 

[##_Image|kage@d0Bogb/btq4hq1wLbt/jEuelGTNA4iRSHLCT0Jdb0/img.jpg|alignCenter|data-origin-width="650" data-origin-height="269" data-ke-mobilestyle="widthContent"|https://learnopencv.com/understanding-alexnet/||_##]

### \# 3. The Architecture 

 중요도 순으로 적었다고 한다

#### @ 3.1 ReLU Nonlinearity

 사실 렐루를 처음 도입한게 알렉스 넷이라는 게 나는 나름 shock 했다. 여기서 나온 거였어? 싶었음.. 

 기존에 사용하던 $\\f(x)=tanh(x)$ 나 시그모이드 함수인 $\\f(x) = \\frac{1}{1 + e^{-x}}$은 saturating nonlinearity 함수로, 학습하는데 오래 걸릴뿐 아니라 기울기 소실의 염려가 있는 함수였다. 그래서 알렉스가? 알렉스 팀이? 고안한 것이 바로 non-saturating nonlinearity인 렐루 함수다. 

[##_Image|kage@bLCvRB/btq6TzXDO5Z/NbnyH1jPEwoFxsqeW1mAYk/img.png|alignCenter|data-origin-width="309" data-origin-height="625" data-ke-mobilestyle="widthOrigin"|||_##]

 saturating nonlinearity 함수가 무엇이냐면 함수값이 어떤 구간으로 bound 지어져 있는 애들이다. 예컨대, 시그모이드 함수가 (0, 1)로 한정되어 있는 것처럼. 즉 x가 무한대로 발산하더라도, y값은 어떤 구간 밖으로 벗어나지 않는다. 시그모이드 함수는 함수값이 0이나 1에 가까워질수록 기울기가 0에 가까워지고,그래서 기울기 소실이 일어난다. 

 렐루 함수의 경우에는 만약 input이 양수라면 $f(x) = x$인 반면 음수라면 그냥 0의 값을 가진다. 따라서 x 값이 발산하면 그냥 x 값을 따라 함수값도 발산해버린다. 또 음수인 input을 받으면 그냥 0의 값이 나오는 것은 우리가 지금 무얼하는지 생각해보면 당연한 결과다.

 feature map에서 음수가 나왔다? 그럼 그냥 다 0 으로 돌려버리는 것이다. pixel값이 음수일 수는 없으니까 ! (\*픽셀은 (0, 255)의 값을 가진다. )

 아래의 사진은 epoch에 따른 traing error의 비율이다. 실선이 렐루, 점선이 탄젠트 함수다. 보면 동일한 에러 비율에 도달하기 위해서 소요되는 epoch이 렐루의 경우 훨씬 적은 것을 알 수 있다. 

[##_Image|kage@bU9WuK/btq4bYZSTmG/tjpn2wAQfFkmAx8rFWMyOk/img.png|alignCenter|data-origin-width="260" data-origin-height="425" width="339" height="NaN" data-ke-mobilestyle="widthContent"|ImageNet Classification with Deep Neural Networks Figure 1||_##]

#### @ 3.2 Training on Multiple GPUs

~ 사실 요즈음은 이렇게 안 한다고 하지만...와 갑자기 짬뽕 먹고 싶다~

GPU를 이용해서 병렬 계산을 하는 것이다. 이는 학습 시간을 줄이는 것과 연관이 있다. 

커널의 반씩을 각각 GPU1, GPU2에 배분하여 학습한다. 다만 하나의 합성곱 층에서 두 GPU가 통신하도록 하는데, 이가 곧 layer 3다. 사진으로 보면 더 이해가 된다. 

[##_Image|kage@bD93hE/btq4bYZSZ7i/FkrwevRNsX3XWFf6t6lI6k/img.png|alignCenter|data-origin-width="679" data-origin-height="228" data-ke-mobilestyle="widthContent"|||_##]

 보면 layer 3에서만 GPU끼리 꼬여서 합성곱 계산을 하는 것을 알 수 있다. 그 외에서는 일절 통신하지 않는다. 

 이건 뒤의 6절에서 나오는 내용이지만, GPU1에는 색과 무관한 커널이 있는 반면, GPU2에는 색에 대한 정보에 관한 커널이 있다고 한다. 

[##_Image|kage@TUCNU/btq4hrsGqeG/ePKH1j1ceAPg2283shj7P1/img.png|alignCenter|data-origin-width="496" data-origin-height="421" data-ke-mobilestyle="widthContent"|&nbsp;Figure 3||_##]

#### @ 3.3 Local Response Normalization 줄여서 LRN

 인공지능 뉴런이 우리 인간의 뇌를 따라한 것이라면, 이 섹션 역시 인간의 뇌에서 아이디어를 얻어서 구현된 부분이다.

 respose normalization 이라고 하는데, 활성화된 뉴런이 주변 이웃 뉴런을 억누르는 현상이라고 한다. 강한 자극이 약한 자극을 전달되는 것을 막는 셈이다. 

[##_Image|kage@SgvbV/btq4eKfaiiE/fuKRHqUBcjvKQxkhCIlibk/img.jpg|alignCenter|data-origin-width="880" data-origin-height="769" data-ke-mobilestyle="widthContent"|https://well-buying.com/free/90808||_##]

~어렸을 때 봤을 법한 밈.. 근데 왜 검색하니까 성인인증이 떴을까..~

딱 이 밈이 적절한 예시다. 우리가 4개를 보는 순간 다른 8개는 보이지 않는다. 활성화된 곳들이 다른 곳을 못 보게끔 억누르기 때문이다. 이를 차용해서 우리의 모델에 적용시켰다.

> "creating competition for big activities amongst neuron outputs computed using different kernels."

[##_Image|kage@bi8gvS/btq4f9Thzqs/zp03hv3lkhlayun3PXHKlk/img.png|alignCenter|data-origin-width="553" data-origin-height="124" data-ke-mobilestyle="widthContent"|LaTex로 바꾸기엔 너무 복잡한 수식...ㅜㅜ||_##]

(x,y) 는 좌표값

b는 정규화된 값이고 n은 고려할 주위 뉴런의 갯수다. 

[##_Image|kage@GyYxe/btq4eiizLLN/H5CCsuxLVZxhm7xltazGik/img.png|alignCenter|width="664" height="132" data-origin-width="664" data-origin-height="132" data-ke-mobilestyle="widthContent"|||_##]

 쉽게 이해하자면

 - feature map 의 (x, y) 값은 높은데 주위 값들은 낮다면 => input 값만 돋보이도록한다. 

 - feature map 의 (x, y) 값은 높은데 주위 값들도 높다면 = > 정규화 시켜줘서 다 낮아지도록 수정한다.

근데 실은 별 효과가 없다고 다른 논문에서 없어진 기법이다. 

#### @ 3.4 overlapping pooling

 제일 쉽다! 풀링하는 영역을 우리는 다 배타적으로 해줬다면, 이 경우는 오히려 겹쳐서 풀링하겠다는 것이다.

 과적합 방지를 위해서 사용한다. 그림으론 아래와 같다 ~너무 대충그렸나..~

[##_Image|kage@MAIlA/btq4hp9qfIj/SZn6g2Aa9KFJwk5rTIp2mk/img.png|alignCenter|width="322" height="129" data-origin-width="322" data-origin-height="129" data-ke-mobilestyle="widthContent"|||_##]

예를 들어, 지금 풀링 사이즈가 2\*2라면 

왼쪽의 경우: 스트라이드(이동 범위)를 2로 설정해서 안 겹치도록 한 것이고

오른쪽의 경우: 스트라이드(이동 범위)를 1로 설정해서 겹치도록 한 것이다. 

#### @ 3.5 overall architecture

 사진을 보면서 지금까지 달려온 것을 정리하도록..

[##_Image|kage@Upc4V/btq4f87TY74/KNW6ku8UUokrLNgDsQALI0/img.png|alignCenter|data-origin-width="513" data-origin-height="336" width="686" height="NaN" data-ke-mobilestyle="widthContent"|||_##]

###   
\# 4. Reducing Overfitting

딥러닝의 가장 큰 이슈다 과적합!

#### @ 4.1 Data Augmentation

기본적으로 과적합을 방지하기 위해서는 데이터 셋을 늘리면 된다. 그렇지만 주어진 데이터 셋은 한정되어 있으니, 본 논문에서는 데이터 셋을 변형하여 임의로 늘리기로 했다. 물론 이렇게 되면 데이터 셋이 독립적이지 않은데 그건 어떻게 해결했는지, 상관이 없는건지는 모르겠다. 본 작업은 CPU로 했다고 하는데.

  1.  generating image transaltion and horizontal reflections: 임의로 사진에서 224 \*224 로 여러번 잘라서 데이터 셋을 키움

(그래서 제일 처음 input이 224\*224\*3 이다 3은 RGB) 

자세히 보면 고양이 위치가 조금씩 다르다 

[##_Image|kage@dHQtdb/btq4bsNW3i1/1guPz8MnrZmbL2qnKUFvg0/img.jpg|alignCenter|data-origin-width="650" data-origin-height="366" data-ke-mobilestyle="widthContent"|||_##]

  2. altering intensities of RGB channels : RGB 값을 변형시켜서 데이터 셋을 키움 

(단 이때,  PCA를 이용함 PCA를 이용해서 데이터의 본질적인 부분, 특징은 최대한 보존하고 그 외의 것들을 transform)

#### @ 4.2 Dropout

[hyelimkungkung.tistory.com/13?category=935192](https://hyelimkungkung.tistory.com/13?category=935192)

여기에 써놨지만, 다시 적어보자면

>   
> 뉴런을 모두 사용하자 않고, 일정 비율만큼만 랜덤으로 골라 사용한다.   
> 그러나 이 방식은 신경만 학습 시에만 사용하고, 예측 시에는 사용하지 않는다.  
>   
> 이를 통해서 얻는 효과는  
>   
>  1. 특정 뉴런, 조합에만 의존적인 것 방지  
>  2. 매번 랜덤적으로 선택하기에, 매번 다른 신경망들이 형성된다 그러나 예측 시에는 모두를 사용하기 때문에 결과적으로 앙상블한 효과가 나타난다   
>   

이렇다. 

0.5의 확률로 dropout을 실시했다. 

(그런데 위에서는 사용하지 않는다고 했지만, 수학적으로 표현하면 가중치가 0인 경우다) 

[##_Image|kage@bLHYQI/btq4dLSWDY2/xRjKzP7MMuGP0IKkln6pL0/img.gif|alignCenter|data-origin-width="551" data-origin-height="281" data-ke-mobilestyle="widthContent"|https://learnopencv.com/understanding-alexnet/||_##]

### \# 5. Details of learning

~아이고 힘들어..~

@ 확률적 경사 하강법 이용

일단 기본적으로 확률적 경사 하강법stochastic gradient descent 을 사용하고 있다. 

경사 하강법에 대해서 저어번에 말했었지만 그 종류가 알고보니 다양하더라. 

실은 요즘은 Adam을 많이 쓴다고 하는데, Adam은 일반화가 어렵다고 한다. 

여하튼, 이 논문에서는 SGD를 사용하고 있다. 

 기본적인 가중치는 아래와 같이 업데이트 된다. 이전 단계의 가중치에 어떤 값을 더해준다. 

 이 값도 매번 업데이트 되는 값인데 또 그 아래에 나와 있는 대로다.

[##_Image|kage@bFHEEn/btq4ceV6gIH/CHKPa6v3CoKpSeYRHD93s0/img.png|alignCenter|width="543" height="239" data-origin-width="543" data-origin-height="239" data-ke-mobilestyle="widthContent"|||_##]

momentum 이라는 건 관성인데, 어떤 방향으로 계속 움직인다면 점점 관성을 줘서 더 크게 움직인다는 것이다. 

weight decay는 과적합을 막기 위해서 사용하는 term이다. 과적합을 하면 대부분 train set에서 엄청난 정답률을 얻을 수 있는 대신 새로운 데이터 셋에서는 제대로 된 예측을 못하므로, 이를 방지하고자 하는데. 실은 과적합은 변수가 지나치게 많아서 모델이 복잡해짐에 따라 발생하는 문제다. 그래서 가중치의 수를 적절하게 조절하기 위해서 우리가 앞서 L2 regularization 했던 것이다. 하여간에, 결국은 모델의 복잡도를 제어하는 term이다. 

마지막은 우리가 아는 그 gradient이다. 배치 별 gradient를 계산해서 평균 낸 값이다. 

@ 가중치 초기화

 $w ~ mathrm{N}(0, (0.01)^{2})$ 

정규분포를 따른다는 가정하에서 랜덤하게 w를 추출해서 초기의 가중치 값을 설정한다

@ learning rate

모든 층에 동일하게 설정한다

만약 validation set의 오류가 epoch이 진행됐는데도 감소하지 않는다면, learning rate는 10으로 나누어 다시 시작한다

본 논문에서는 0.01로 시작해서 3번의 수정을 거쳤다고 한다(0.0001)

\=> 그랬는데도 결과를 얻는데 5~6일이 걸렸다 하네요..푸하하

만약 변수 하나를 잘못 써서 처음부터 가야 한다고 생각하면 끔찍 

### \# 6. Results

객관적인 수치로는 

[##_Image|kage@tF3qU/btq4dciVF4l/3WjNIEn3YeyDcyBKlI1A20/img.png|alignCenter|data-origin-width="458" data-origin-height="162" data-ke-mobilestyle="widthContent"|||_##]

위의 두 가지에 비해서 CNN을 보면 획기적으로 줄었다는 것을 알 수 있다. 

구체적인 디테일을 보면 

[##_Image|kage@KqgdW/btq4c1vbISD/nOTzsZLqZCk0Su6BO6VKq1/img.png|alignCenter|data-origin-width="528" data-origin-height="467" data-ke-mobilestyle="widthContent"|||_##]

위는 test set의 이미지를 본 논문에서 사용한 모델을 적합시킴에 따라 나온 결과다

본 그림의 결론을 요약하면 

  @ 1 구석에 있는 이미지 (off center) 역시 분류를 잘 수행한다는 점이다 ~ mite

  @ 2 실제로도 모호한 이미지의 경우에 잘 예측이 안 됐다 ~ 위의 달마시안/ 체리의 경우

(나같아도 헷갈릴듯)

[##_Image|kage@A6HLJ/btq4hH3gzet/kpo6OnkopQavKAfjEkhxLK/img.png|alignCenter|data-origin-width="576" data-origin-height="423" data-ke-mobilestyle="widthContent"|||_##]

위의 이미지에서 첫번쩨 세로에 있는 5개의 그림들은 test set에 있는 이미지이고 

그 이후의 6\*5는 train 에 있는 이미지 중 test set의 이미지와 가장 유사한 것들이다

이때 유사함의 척도는 유클리디안 거리다

### \# 7. Discussions

 이 대목에서 사실상 새로운 걸 제시한다기 보다는... 내가 느끼기에는 크게 두가지다

 1. 합성곱 층을 하나라도 빼면 성능이 저하되니까 빼지 마라 2. 더 좋은 GPU가 나오면 성능이 개선될 것이다

@ 구현

 사실 앞에서 한 CNN이랑 다를게 없다...

 내가 느낀 건... CNN은 input과 output 이미지의 사이즈만 잘 계산하면 torch가 너무 좋아서 다 해준다는 거다...

 개입할 여지가 별로 없군..

 실상 머신러닝보다 딥러닝이 더 쉬운 것 같기도 하고~.. 라고 초짜가 말했다~

 그래서 그냥 접은 글로 넣는다

더보기

```
import torch
import torch.nn as nn
import torch.nn.init


learning_rate = 0.00001


class AlexNet(nn.Module):
    def __init__(self):
        super(AlexNet, self).__init__()
        self.cnnnet = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=96, kernel_size=11, stride=4),
            nn.ReLU(),
            nn.LocalResponseNorm(5, 0.0001, 0.75, 2),
            nn.MaxPool2d(3, 2),

            nn.Conv2d(in_channels=96, out_channels=256, kernel_size=5),
            nn.ReLU(),
            nn.LocalResponseNorm(5, 0.0001, 0.75, 2),
            nn.MaxPool2d(3, 2),

            nn.Conv2d(in_channels=256, out_channels=384, kernel_size=3),
            nn.ReLU(),

            nn.Conv2d(in_channels=384, out_channels=384, kernel_size=3),
            nn.ReLU(),

            nn.Conv2d(in_channels=384, out_channels=256, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(3, 2),
        )

        self.fclayer = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Linear(4096,100)
        )

        self.init_bias()

    def init_bias(self):
        for layer in self.cnnnet:
            if isinstance(layer, nn.Conv2d):
                nn.init.normal_(layer.weight, mean=0, std=0.01)
                nn.init.constant_(layer.bias, 0)

        nn.init.constant_(self.cnnnet[4].bias, 1)
        nn.init.constant_(self.cnnnet[10].bias, 1)
        nn.init.constant_(self.cnnnet[12].bias, 1)

    def foward(self, x):
        output = self.cnnnet(x)
        output = output.view(output.size(0), -1)
        output = self.fclayer(output)
        return output

Alex = AlexNet()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(Alex.parameters(), lr=learning_rate, momentum=0.9, weight_decay=0.0005)



```

참고한 자료들

0\. 무엇보다도 핵심인 원문 : [papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)

[1\. 원문도 그대로 실어서 해석에도 도움이 되고 기타 부가 설명도 많아서 좋은 포스팅!! : 89douner.tistory.com/60](https://89douner.tistory.com/60)

2\. data augmentation 에 대해서 도움이 된 글: [blog.naver.com/PostView.nhn?blogId=intelliz&logNo=221743351934](http://blog.naver.com/PostView.nhn?blogId=intelliz&logNo=221743351934)

3\. 이미지에 대한 이해(픽셀에 관해서 알고 싶다면): [twlab.tistory.com/23](https://twlab.tistory.com/23)

4\. section 5와 관련해서 보기 좋은 포스팅: [hiddenbeginner.github.io/deeplearning/paperreview/2019/12/29/paper\_review\_AdamW.html](https://hiddenbeginner.github.io/deeplearning/paperreview/2019/12/29/paper_review_AdamW.html)

5\. 이미지 부자: [learnopencv.com/understanding-alexnet/](https://learnopencv.com/understanding-alexnet/)

6.  (구현) nn.Dropout(inplace=True)에 대해서 헤매게 한 [deep-learning-study.tistory.com/376](https://deep-learning-study.tistory.com/376)

7.  (구현) [wolfy.tistory.com/241](https://wolfy.tistory.com/241)

#### @ 사족

논문 9쪽자리 보는 것도 너무 긴데 다음은 20쪽 자리다... too long 엄청난 나...

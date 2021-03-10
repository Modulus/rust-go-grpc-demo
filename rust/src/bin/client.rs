
use say::sayer_client::SayerClient;
use say::SayerRequest;

pub mod say {
    tonic::include_proto!("say");
}


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = SayerClient::connect("http://[::1]:50051").await?;

    let request = tonic::Request::new(SayerRequest {
        name: "Tonic".into(),
        comment: "This is my first try".into()
    });

    let response = client.send(request).await?;

    println!("RESPONSE={:?}", response);

    let inner_response = response.into_inner();

    println!("Message: {:?}", inner_response.message);
    println!("Comment: {:?}", inner_response.comment);
    println!("Id: {:?}", inner_response.id);


    Ok(())
}
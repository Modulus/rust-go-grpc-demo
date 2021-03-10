
use tonic::{transport::Server, Request, Response, Status};

use say::sayer_server::{Sayer, SayerServer};
use say::{SayerResponse, SayerRequest};


pub mod say {
    tonic::include_proto!("say");
}

#[derive(Default)]
pub struct MySayer {}

#[tonic::async_trait]
impl Sayer for MySayer {
    async fn send(
        &self,
        request: Request<SayerRequest>,
    ) -> Result<Response<SayerResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        let request_inner = request.into_inner();

        println!("Request contained: name: {:?} and comment: {:?}", &request_inner.name, &request_inner.comment);

        println!("Returning: {:?}", format!("Hello {}!", request_inner.name));
        let reply = say::SayerResponse {
            message: format!("Hello {}!", request_inner.name),
            comment: format!("Comment: {}", request_inner.comment),
            id: 123
        };
        Ok(Response::new(reply))
    }
}


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:50051".parse().unwrap();
    let greeter = MySayer::default();

    println!("GreeterServer listening on {}", addr);

    Server::builder()
        .add_service(SayerServer::new(greeter))
        .serve(addr)
        .await?;

    Ok(())
}


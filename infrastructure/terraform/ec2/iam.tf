resource "aws_iam_role" "normalisation_borne_electrique" {
  name = "normalisation_borne_electrique"

    assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

  tags = {
    tag-key = "webinar"
  }
}

resource "aws_iam_instance_profile" "normalisation_borne_electrique" {
  name = "normalisation_borne_electrique"
  role = aws_iam_role.normalisation_borne_electrique.name
}

resource "aws_iam_role_policy" "normalisation_borne_electrique" {
  name = "normalisation_borne_electrique"
  role = aws_iam_role.normalisation_borne_electrique.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}

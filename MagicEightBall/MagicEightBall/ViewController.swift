//
//  ViewController.swift
//  MagicEightBall
//
//  Created by Jonathan Kopp on 10/25/18.
//  Copyright © 2018 Jonathan Kopp. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var shakeButton: UIButton!
    @IBOutlet weak var answerLabel: UILabel!
    let answers = ["Yes, definitely", "It is certain", "Without a doubt", "Yes", "Most likely", "Sure, why not?", "Same", "Tell me more", "Out to lunch", "Reply hazy, try again", "Ask again later", "The cake is a lie", "42", "TMI", "Very doubtful", "Don't count on it", "My reply is no", "Absolutely not"]

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    @IBAction func shakeButtonTapped(_ sender: UIButton) {
        generateAnswer()
    }
    override func motionBegan(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
        guard motion == .motionShake
            else {return }
        self.funColorTime()
    }
    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
        guard motion == .motionShake
            else {
            return }
        
        generateAnswer()
    }
    func funColorTime()
    {
               // print("Called")
                let ran1 = CGFloat(arc4random_uniform(UInt32(255 - 0 + 1)))
                let ran2 = CGFloat(arc4random_uniform(UInt32(255 - 0 + 1)))
                let ran3 = CGFloat(arc4random_uniform(UInt32(255 - 0 + 1)))
                let col = UIColor(red: ran1/255, green: ran2/255, blue: ran3/255, alpha: 1)
        self.view.backgroundColor = col
            
    }
    func generateAnswer() {
        let maxIndex = UInt32(answers.count)
        let randomIndex = Int(arc4random_uniform(maxIndex))
        
        answerLabel.text = answers[randomIndex]
    }
}

